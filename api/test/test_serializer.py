from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import CheckBox
from api.serializers import CheckBoxSerializers

class CheckboxSerializerAPiTestCase(APITestCase):
    def test_serializer(self):
        checkbox_1 = CheckBox.objects.create(name='checkbox_1')
        checkbox_2 = CheckBox.objects.create(name='checkbox_2')
        serializer_data = CheckBoxSerializers([checkbox_1, checkbox_2], many=True).data
        expected_data = [
            {
                "id": 1,
                "name": "checkbox_1",
                "is_checked": False
            },
            {
                "id": 2,
                "name": "checkbox_2",
                "is_checked": True
            }
        ]
        self.assertEqual(serializer_data, expected_data)