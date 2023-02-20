from rest_framework import serializers

from project.serializers import (
    ModelFieldMinimalSerializer,
)

from core.models import (
    DateFieldConfig,
    FloatFieldConfig,
    IntegerFieldConfig,
    CharFieldConfig,
    FileFieldConfig,
    ForeignKeyFieldConfig,
    UploadSize,
    ContentTypes,
)


class DateFieldConfigSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = DateFieldConfig
        fields = ('id', 'type', 'auto_now',
                  'auto_now_add', 'model_field')


class DateFieldConfigDataSerializer(serializers.ModelSerializer):
    model_field = ModelFieldMinimalSerializer()
    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = DateFieldConfig
        fields = ('id', 'type', 'auto_now',
                  'auto_now_add', 'model_field',
                  'created_at')


class FloatFieldConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = FloatFieldConfig
        fields = ('id', 'min_value', 'max_value',
                  'max_digits', 'decimal_places',
                  'model_field')


class FloatFieldConfigDataSerializer(serializers.ModelSerializer):
    model_field = ModelFieldMinimalSerializer()

    class Meta:
        model = FloatFieldConfig
        fields = ('id', 'min_digits', 'max_digits',
                  'decimal_places', 'model_field',
                  'created_at')


class IntegerFieldConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntegerFieldConfig
        fields = ('id', 'min_value', 'max_value',
                  'only_positive', 'big_integer',
                  'model_field')


class IntegerFieldConfigDataSerializer(serializers.ModelSerializer):
    model_field = ModelFieldMinimalSerializer()

    class Meta:
        model = IntegerFieldConfig
        fields = ('id', 'min_value', 'max_value',
                  'only_positive', 'big_integer',
                  'model_field', 'created_at')


class CharFieldConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharFieldConfig
        fields = ('id', 'max_length', 'regex_pattern',
                  'model_field')


class CharFieldConfigDataSerializer(serializers.ModelSerializer):
    model_field = ModelFieldMinimalSerializer()

    class Meta:
        model = CharFieldConfig
        fields = ('id', 'max_length', 'regex_pattern',
                  'model_field', 'created_at')


class ForeignKeyFieldConfigSerializer(serializers.ModelSerializer):
    relation_type = serializers.CharField(source='get_relation_type_display')

    class Meta:
        model = ForeignKeyFieldConfig
        fields = ('id', 'relation_type', 'on_delete',
                  'model_field')


class ForeignKeyFieldConfigDataSerializer(serializers.ModelSerializer):
    model_field = ModelFieldMinimalSerializer()
    relation_type = serializers.CharField(source='get_relation_type_display')

    class Meta:
        model = ForeignKeyFieldConfig
        fields = ('id', 'relation_type', 'on_delete',
                  'model_field', 'created_at')


class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentTypes
        fields = ('id', 'name', 'content_types')


class UploadSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadSize
        fields = ('id', 'name', 'size')


class FileFieldConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileFieldConfig
        fields = ('id', 'upload_to', 'max_length',
                  'content_types', 'max_upload_size',
                  'model_field')


class FileFieldConfigDataSerializer(serializers.ModelSerializer):
    model_field = ModelFieldMinimalSerializer()
    content_types = ContentTypeSerializer(many=True)
    max_upload_size = UploadSizeSerializer()

    class Meta:
        model = FileFieldConfig
        fields = ('id', 'upload_to', 'max_length',
                  'content_types', 'max_upload_size',
                  'model_field', 'created_at')
