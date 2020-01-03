from django.urls import include, path
from . import views

urlpatterns = [
    # path("login", views.login, name="login"),
    # path('', views.UserListView.as_view(), name="UserList"),
    path('student/create', views.StudentCreateView.as_view(), name="StudentCreate"),
    path('parent/create', views.ParentCreateView.as_view(), name="ParentCreate"),
    path('bloodbank/create', views.BloodBankCreateView.as_view(),
         name="BloodBankCreate"),
    path('hospital/create', views.HospitalCreateView.as_view(),
         name="HospitalCreate"),
    path('rest-auth/', include('rest_auth.urls')),
]
