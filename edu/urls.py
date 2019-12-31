from django.urls import path
from . import views
urlpatterns = [
    path('', views.NoteList.as_view(), name='NoteList'),
    path('<int:pk>/', views.NoteRetrieve.as_view(), name='NoteRetrieve'),
    path('<int:pk>/NoteDestroy', views.NoteDestroy.as_view(), name='NoteDestroy'),
    path('<int:pk>/NoteUpdate', views.NoteUpdate.as_view(), name='NoteUpdate'),
    path('<int:pk>/NoteRetUp', views.NoteRetUp.as_view(), name='NoteRetUp'),
    path('NoteCreate', views.NoteCreate.as_view(), name='NoteCreate'),
]
