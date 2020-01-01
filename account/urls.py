from django.urls import include, path
from . import views

urlpatterns = [
    # path("login", views.login, name="login"),
    # path('', views.UserListView.as_view(), name="UserList"),
    path('create', views.UserCreateView.as_view(), name="UserCreate"),
    path('rest-auth/', include('rest_auth.urls')),
]
