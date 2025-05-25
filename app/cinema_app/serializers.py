from rest_framework import serializers
from .models import Viewer


class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        fields = ['name', 'email']
