from rest_framework import serializers
from .models import NonConformity


class NonConformitySerializer(serializers.ModelSerializer):
    class Meta:
        model = NonConformity
        fields = [
            'company_id', 'site_id', 'reported_by',
            'issue_type', 'description', 'photos', 'severity',
            'tags', 'custom_fields', 'status', 'comments']
        extra_kwargs = {
            'photos': {'required': False},
            'tags': {'required': False},
            'custom_fields': {'required': False},
            'comments': {'required': False},
        }
