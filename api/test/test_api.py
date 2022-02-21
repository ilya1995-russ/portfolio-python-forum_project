from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import CheckBox
# from collections import OrderedDict
from api.serializers import CheckBoxSerializers

class CheckboxApiTestCase(APITestCase):
    # def test_get(self):
    #     url = reverse('checkbox-list')
    #     print(url)
    #     response = self.client.get(url)
    #     print(response.data)
    
    #    def test_get(self):
    #     checkbox_1 = CheckBox.objects.create(name='checkbox_1')
    #     checkbox_2 = CheckBox.objects.create(name='checkbox_2')
    #     url = reverse('checkbox-list')
    #     response = self.client.get(url)
    #     print(response.data)

        # def test_get(self):
        #     checkbox_1 = CheckBox.objects.create(name='checkbox_1')
        #     checkbox_2 = CheckBox.objects.create(name='checkbox_2')
        #     url = reverse('checkbox-list')
        #     response = self.client.get(url)
        #     data = OrderedDict([('count', 2), ('next', None), ('previous', None),
        #      ('results', [OrderedDict([('name', 'checkbox_1'), ('is_checked', False), ('title', 'checkbox_1 python')]),
        #       OrderedDict([('name', 'checkbox_2'), ('is_checked', False), ('title', 'checkbox_2 python')])])])
        #     self.assertEqual(response.data, data)
        
    def test_get(self):
        checkbox_1 = CheckBox.objects.create(name='checkbox_1')
        checkbox_2 = CheckBox.objects.create(name='checkbox_2')
        url = reverse('checkbox-list')
        response = self.client.get(url)
        serializer_data = CheckBoxSerializers([checkbox_1, checkbox_2], many=True).data
        self.assertEqual(response.data, serializer_data)

    def test_create(self):
        data = {
            "name": "checkbox_3"
        }
        url = reverse('checkbox-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)



