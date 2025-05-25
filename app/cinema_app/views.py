from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Viewer
from .serializers import ViewerSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the application index.")


class ViewersView(APIView):
    def get(self, request):
        viewers = Viewer.objects.all()
        serializer = ViewerSerializer(viewers, many=True)
        return Response(serializer.data)
