from django.urls import path
from . import views

urlpatterns = [
    path("", views.SchemeSerializerView.as_view(), name="SchemeSerializer"),
]
