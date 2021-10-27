from django.urls import path, include
from rest_framework import routers, views
from api.views import CheckBoxViewsSet
from api import views

router = routers.DefaultRouter()
router.register('checkbox', CheckBoxViewsSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('checkbox_list', views.checkbox_list, name="checkbox_list"),
    # path('checkbox_list/<int:pk>', views.checkbox_detail, name="checkbox_detail"),
    # path('checkbox_create', views.checkbox_create, name="checkbox_create"),
    # path('checkbox_update/<int:pk>', views.checkbox_update, name="checkbox_update"),
    # path('checkbox_delete/<int:pk>', views.checkbox_delete, name="checkbox_delete"),
    # path('checkbox_list', views.CheckBoxList.as_view(), name="checkbox_list"),
    # path('checkbox_detalied/<int:pk>', views.CheckBoxDetailed.as_view(), name="checkbox_detalied")
    path('data', views.DataView.as_view(), name="data"),
]