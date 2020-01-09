from django.urls import path
from . import views
urlpatterns = [
    path('HospitalDetailList', views.HospitalDetailList.as_view(),
         name='HospitalDetailList'),
    path('HospitalDetailCreate',
         views.HospitalDetailCreate.as_view(), name='HospitalDetailCreate'),
    path('DepttList', views.DepttList.as_view(), name='DepttList'),
    path('DepttCreate', views.DepttCreate.as_view(), name='DepttCreate'),
    path('DoctorDetailList', views.DoctorDetailList.as_view(),
         name='DoctorDetailList'),
    path('DoctorDetailCreate', views.DoctorDetailCreate.as_view(),
         name='DoctorDetailCreate'),
    path('AmbulanceList', views.AmbulanceList.as_view(),
         name='AmbulanceList'),
    path('AmbulanceCreate', views.AmbulanceCreate.as_view(),
         name='AmbulanceCreate'),
    path('BloodStockList', views.BloodStockList.as_view(),
         name='BloodStockList'),
    path('BloodStockCreate', views.BloodStockCreate.as_view(),
         name='BloodStockCreate'),
]
