from django.db.models import fields
from rest_framework import serializers
from api.models import CheckBox

class CheckBoxSerializers(serializers.ModelSerializer):

    title = serializers.SerializerMethodField()
    class Meta:
        model = CheckBox
        fields = ['name', 'is_checked', 'title']
    @staticmethod
    def get_title(object):
        return object.name + " " + "python"

class DataSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    attrs = serializers.JSONField(required=False)
    type = serializers.CharField(required=False)
    val_1 = serializers.IntegerField()
    val_2 = serializers.IntegerField()

    @staticmethod
    def validated_type(type):
        if not type in ['dict', 'list', 'tuple']:
            raise serializers.ValidationError(f"{type} is not allowed")
        return type



