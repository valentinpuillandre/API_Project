from rest_framework import serializers
from .models import NonConformity, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class NonConformitySerializer(serializers.ModelSerializer):
    class Meta:
        model = NonConformity
        fields = [
            'company_id', 'site_id', 'reported_by',
            'issue_type', 'description', 'photos', 'severity',
            'tags', 'custom_fields', 'status', 'comments']
