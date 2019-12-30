from django.http import HttpResponse
import json
import requests
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from .serializers import (
    SubjectSerializer,
    ClassSerializer,
    TopicSerializer,
    ModuleSerializer,
    QuestionSerializer,
    ChoiceSerializer,
    ScoreSerializer
)
from .models import Subject, Class, Topic, Module, Question, Choice, Score


class SubjectList(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectCreate(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    # def perform_create(self,serializer):
    #     serializer.save(user=self.request.user)


class SubjectRetrieve(RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectUpdate(UpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectRetUp(RetrieveUpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDestroy(DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

##/////##/////##/////##/////##/////##/////##/////##/////##/////##/////##


class ClassList(ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassCreate(CreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    # def perform_create(self,serializer):
    #     serializer.save(user=self.request.user)


class ClassRetrieve(RetrieveAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassUpdate(UpdateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassRetUp(RetrieveUpdateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassDestroy(DestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


##/////##/////##/////##/////##/////##/////##/////##/////##/////##/////##


class TopicList(ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['@module__id']
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicCreate(CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicRetrieve(RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicUpdate(UpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicRetUp(RetrieveUpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDestroy(DestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


##/////##/////##/////##/////##/////##/////##/////##/////##/////##/////##


class ModuleList(ListAPIView):
    serializer_class = ModuleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['@subject__id']
    queryset = Module.objects.all()


class ModuleCreate(CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleRetrieve(RetrieveAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleUpdate(UpdateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleRetUp(RetrieveUpdateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleDestroy(DestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


##/////##/////##/////##/////##/////##/////##/////##/////##/////##/////##


class QuestionList(ListAPIView):
    queryset = Question.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['@topic__id']
    serializer_class = QuestionSerializer


class QuestionCreate(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieve(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionUpdate(UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetUp(RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDestroy(DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

##/////##/////##/////##/////##/////##/////##/////##/////##/////##/////##


class ChoiceList(ListAPIView):
    queryset = Choice.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['@question__id']
    serializer_class = ChoiceSerializer


class ChoiceCreate(CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceRetrieve(RetrieveAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceUpdate(UpdateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceRetUp(RetrieveUpdateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDestroy(DestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

##/////##/////##/////##/////##/////##/////##/////##/////##/////##/////##


class ScoreList(ListAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class ScoreCreate(CreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class ScoreRetrieve(RetrieveAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class ScoreUpdate(UpdateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class ScoreRetUp(RetrieveUpdateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class ScoreDestroy(DestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


##/////##/////##/////##/////##/////##/////##/////##/////##/////##/////##


def quizs(request):
    url = "https://quiz-rest.herokuapp.com/?format=json"
    res = requests.get(url)
    data = res.text
    pdata = json.loads(data)

    return HttpResponse(pdata[1]['id'])
