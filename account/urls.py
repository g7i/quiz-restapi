from django.urls import include, path
from . import views

urlpatterns = [
    # path("login", views.login, name="login"),
    # path('', views.UserListView.as_view(), name="UserList"),
    path('student/create', views.StudentCreateView.as_view(), name="StudentCreate"),

    path('teacher/create', views.TeacherCreateView.as_view(), name="TeacherCreate"),

    path('school/create', views.SchoolCreateView.as_view(), name="SchoolCreate"),

    path('<str:key>/school',
         views.SchoolRetrieveView.as_view(), name="SchoolRetrieve"),

    path('parent/create', views.ParentCreateView.as_view(), name="ParentCreate"),

    path('bloodbank/create', views.BloodBankCreateView.as_view(),
         name="BloodBankCreate"),

    path('hospital/create', views.HospitalCreateView.as_view(),
         name="HospitalCreate"),

    path('rest-auth/', include('rest_auth.urls')),
]
