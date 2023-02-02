from rest_framework import serializers
from core.models import DataType


class DataTypeSerializer(serializers.ModelSerializer):
    """Serializer for data type objects"""

    class Meta:
        model = DataType
        fields = ('id', 'name', 'description')
