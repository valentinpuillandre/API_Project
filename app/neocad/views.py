from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import NonConformity
from .serializers import NonConformitySerializer


def index(request):
    return JsonResponse({"status": "ok"})


class NonConformityViewSet(APIView):
    def get(self, request):
        queryset = NonConformity.objects.all()
        serializer_class = NonConformitySerializer(queryset, many=True)
        return Response(serializer_class.data)
