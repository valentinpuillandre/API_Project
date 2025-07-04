from django.http import JsonResponse
from django.views import View
from django.conf import settings
from pymongo import MongoClient

from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.throttling import UserRateThrottle

from .models import NonConformity
from .serializers import NonConformitySerializer
from rest_framework.permissions import IsAuthenticated


class IndexView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})


class TenPerMinuteUserThrottle(UserRateThrottle):
    rate = '10/minute'


class NonConformityListView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [TenPerMinuteUserThrottle]

    @swagger_auto_schema(
        operation_summary="List all nonconformities",
        operation_description=(
            "Retrieve a list of all nonconformities in the system."
        )
    )
    def get(self, request):
        queryset = NonConformity.objects.all()
        serializer = NonConformitySerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new nonconformity",
        operation_description=(
            "Create a new nonconformity by providing the required data."
        )
    )
    def post(self, request):
        serializer = NonConformitySerializer(data=request.data)
        if serializer.is_valid():
            non_conformity = serializer.save()
            full_data = NonConformitySerializer(non_conformity).data
            return Response(full_data, status=201)
        return Response(serializer.errors, status=400)


class NonConformityDetailView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [TenPerMinuteUserThrottle]

    @swagger_auto_schema(
        operation_summary="Retrieve a specific nonconformity",
        operation_description=(
            "Retrieve details of a specific nonconformity using its unique ID."
        )
    )
    def get(self, request, pk):
        try:
            non_conformity = NonConformity.objects.get(pk=pk)
            serializer = NonConformitySerializer(non_conformity)
            return Response(serializer.data)
        except NonConformity.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

    @swagger_auto_schema(
        operation_summary="Update a specific nonconformity",
        operation_description=(
            "Partially update a specific nonconformity using its unique ID."
        )
    )
    def patch(self, request, pk):
        try:
            non_conformity = NonConformity.objects.get(pk=pk)
        except NonConformity.DoesNotExist:
            return Response({"error": "Not found"}, status=404)
        serializer = NonConformitySerializer(
            non_conformity, data=request.data, partial=True
            )
        if serializer.is_valid():
            non_conformity = serializer.save()
            full_data = NonConformitySerializer(non_conformity).data
            return Response(full_data)
        return Response(serializer.errors, status=400)

    @swagger_auto_schema(
        operation_summary="Delete a specific nonconformity",
        operation_description=(
            "Delete a specific nonconformity using its unique identifier (pk)."
        )
    )
    def delete(self, request, pk):
        try:
            non_conformity = NonConformity.objects.get(pk=pk)
            deleted_data = NonConformitySerializer(non_conformity).data
            non_conformity.delete()
            return Response(deleted_data, status=200)
        except NonConformity.DoesNotExist:
            return Response({"error": "Not found"}, status=404)


class NonConformityStatsView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [TenPerMinuteUserThrottle]

    @swagger_auto_schema(
        operation_summary="Get severity statistics",
        operation_description=(
            "Retrieve statistics about the number of nonconformities",
            "per severity level using MongoDB aggregation."
        )
    )
    def get(self, request):
        client = MongoClient(settings.MONGODB_URI)
        db_name = settings.DATABASES['default']['NAME']
        db = client[db_name]
        collection = db['neocad']

        pipeline = [
            {
                "$group": {
                    "_id": "$severity",
                    "count": {"$sum": 1}
                }
            },
            {
                "$sort": {"count": -1}
            }
        ]
        results = list(collection.aggregate(pipeline))
        stats = {item['_id']: item['count'] for item in results}
        return Response(stats)
