#from django.shortcuts import render

from re import L
from rest_framework import viewsets
from api import serializers
from api.models import CheckBox
from api.serializers import CheckBoxSerializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework import generics, mixins

# class CheckBoxViewsSet(viewsets.ModelViewSet):
#     queryset = CheckBox.objects.all()
#     serializer_class = CheckBoxSerializers

class CheckBoxList(generics.ListCreateAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
     # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    queryset = CheckBox.objects.all()
    serializer_class = CheckBoxSerializers
    def get (self, req, *args, **kwargs):
         #users = [user.username for user in User.objects.all()]
        # checkboxes = CheckBox.objects.all()
        # serializer = CheckBoxSerializers(checkboxes, many=True)
        # return Response(serializer.data)
        return self.list(req, *args, **kwargs)
    def post (self, req, *args, **kwargse):
        # serializer = CheckBoxSerializers(data=req.data)
        # if serializer.is_valid():
        #     serializer.save()
        # return Response(serializer.data, status.HTTP_201_CREATED)
        return self.create(req, *args, **kwargse)

# class CheckBoxDetailed(APIView):
#     permission_classes = [permissions.IsAdminUser]

#     def delete(self, req, pk, format=None):
#         checkbox = CheckBox.objects.get(id=pk)
#         checkbox.delete()
#         return Response(status.HTTP_204_NO_CONTENT
# 
class CheckBoxDetailed(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]

    def delete(self, req, pk, format=None):
        checkbox = CheckBox.objects.get(id=pk)
        checkbox.delete()
        return Response(status.HTTP_204_NO_CONTENT)





@api_view(['GET'])
def checkbox_list(req):
    checkboxes = CheckBox.objects.all()
    serializer = CheckBoxSerializers(checkboxes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def checkbox_detail(req, pk):
    try:
        checkboxes = CheckBox.objects.get(id=pk)
        serializer = CheckBoxSerializers(checkboxes)
    except CheckBox.DoesNotExist:
        return Response({"error": f"Checkbox with id={pk} is not founds"}, status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['POST'])
def checkbox_create(req):
    serializer = CheckBoxSerializers(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['PUT'])
def checkbox_update(req, pk):
    try:
        checkbox = CheckBox.objects.get(id=pk)
        serializer = CheckBoxSerializers(checkbox, data=req.data)
        if serializer.is_valid():
            serializer.save()
    except CheckBox.DoesNotExist:
        return Response({"error": f"Checkbox with id={pk} is not founds"}, status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['DELETE'])
def checkbox_delete(req, pk):
    checkbox = CheckBox.objects.get(id=pk)
    checkbox.delete()
    return Response(status.HTTP_204_NO_CONTENT)
