from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import NonConformity, Viewer
from .serializers import NonConformitySerializer, ViewerSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the application index.")


class NonConformityViewSet(APIView):
    def get(self, request):
        queryset = NonConformity.objects.all()
        serializer_class = NonConformitySerializer(queryset, many=True)
        return Response(serializer_class.data)
