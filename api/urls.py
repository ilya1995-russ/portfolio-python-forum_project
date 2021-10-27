from django.urls import path, include
from rest_framework import routers
from api.views import CheckBoxViewsSet

router = routers.DefaultRouter()
router.register('checkbox', CheckBoxViewsSet)


urlpatterns = [
    path('', include(router.urls)),
]