from django.urls import path
from . import views
urlpatterns = [
    path('', views.SubjectList.as_view(),name='SubjectList'),
    path('quizs', views.quizs,name='quizs'),
    path('<int:pk>/',views.SubjectRetrieve.as_view(),name='SubjectRetrieve'),
    path('<int:pk>/SubjectDestroy',views.SubjectDestroy.as_view(),name='SubjectDestroy'),
    path('<int:pk>/SubjectUpdate',views.SubjectUpdate.as_view(),name='SubjectUpdate'),
    path('<int:pk>/SubjectRetUp',views.SubjectRetUp.as_view(),name='SubjectRetUp'),
    path('SubjectCreate',views.SubjectCreate.as_view(),name='SubjectCreate'),


    path('class', views.ClassList.as_view(),name='ClassList'),
    path('class/<int:pk>/',views.ClassRetrieve.as_view(),name='ClassRetrieve'),
    path('class/<int:pk>/ClassDestroy',views.ClassDestroy.as_view(),name='ClassDestroy'),
    path('class/<int:pk>/ClassUpdate',views.ClassUpdate.as_view(),name='ClassUpdate'),
    path('class/<int:pk>/ClassRetUp',views.ClassRetUp.as_view(),name='ClassRetUp'),
    path('class/ClassCreate',views.ClassCreate.as_view(),name='ClassCreate'),


    path('topic', views.TopicList.as_view(),name='TopicList'),
    path('topic/<int:pk>/',views.TopicRetrieve.as_view(),name='TopicRetrieve'),
    path('topic/<int:pk>/TopicDestroy',views.TopicDestroy.as_view(),name='TopicDestroy'),
    path('topic/<int:pk>/TopicUpdate',views.TopicUpdate.as_view(),name='TopicUpdate'),
    path('topic/<int:pk>/TopicRetUp',views.TopicRetUp.as_view(),name='TopicRetUp'),
    path('topic/TopicCreate',views.TopicCreate.as_view(),name='TopicCreate'),

    path('module', views.ModuleList.as_view(),name='ModuleList'),
    path('module/<int:pk>/',views.ModuleRetrieve.as_view(),name='ModuleRetrieve'),
    path('module/<int:pk>/ModuleDestroy',views.ModuleDestroy.as_view(),name='ModuleDestroy'),
    path('module/<int:pk>/ModuleUpdate',views.ModuleUpdate.as_view(),name='ModuleUpdate'),
    path('module/<int:pk>/ModuleRetUp',views.ModuleRetUp.as_view(),name='ModuleRetUp'),
    path('module/ModuleCreate',views.ModuleCreate.as_view(),name='ModuleCreate'),

    path('question', views.QuestionList.as_view(),name='QuestionList'),
    path('question/<int:pk>/',views.QuestionRetrieve.as_view(),name='QuestionRetrieve'),
    path('question/<int:pk>/QuestionDestroy',views.QuestionDestroy.as_view(),name='QuestionDestroy'),
    path('question/<int:pk>/QuestionUpdate',views.QuestionUpdate.as_view(),name='QuestionUpdate'),
    path('question/<int:pk>/QuestionRetUp',views.QuestionRetUp.as_view(),name='QuestionRetUp'),
    path('question/QuestionCreate',views.QuestionCreate.as_view(),name='QuestionCreate'),

    path('choice', views.ChoiceList.as_view(),name='ChoiceList'),
    path('choice/<int:pk>/',views.ChoiceRetrieve.as_view(),name='ChoiceRetrieve'),
    path('choice/<int:pk>/ChoiceDestroy',views.ChoiceDestroy.as_view(),name='ChoiceDestroy'),
    path('choice/<int:pk>/ChoiceUpdate',views.ChoiceUpdate.as_view(),name='ChoiceUpdate'),
    path('choice/<int:pk>/ChoiceRetUp',views.ChoiceRetUp.as_view(),name='ChoiceRetUp'),
    path('choice/ChoiceCreate',views.ChoiceCreate.as_view(),name='ChoiceCreate'),

    path('score', views.ScoreList.as_view(),name='ScoreList'),
    path('score/<int:pk>/',views.ScoreRetrieve.as_view(),name='ScoreRetrieve'),
    path('score/<int:pk>/ScoreDestroy',views.ScoreDestroy.as_view(),name='ScoreDestroy'),
    path('score/<int:pk>/ScoreUpdate',views.ScoreUpdate.as_view(),name='ScoreUpdate'),
    path('score/<int:pk>/ScoreRetUp',views.ScoreRetUp.as_view(),name='ScoreRetUp'),
    path('score/ScoreCreate',views.ScoreCreate.as_view(),name='ScoreCreate'),
]