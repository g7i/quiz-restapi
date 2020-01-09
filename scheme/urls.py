from django.urls import path
from . import views

urlpatterns = [
    path("", views.SchemeSerializerView.as_view(), name="SchemeSerializer"),
    path("csr/list", views.CSRList.as_view(), name="CSRList"),
    path("csr/create", views.CSRCreate.as_view(), name="CSRCreate"),
]
