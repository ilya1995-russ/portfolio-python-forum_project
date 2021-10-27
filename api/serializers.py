from django.db.models import fields
from rest_framework import serializers
from api.models import CheckBox

class CheckBoxSerializers(serializers.ModelSerializer):
    class Meta:
        model = CheckBox
        fields = '__all__'

