from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from .serializers import NoteSerializer, TeacherDetailSerializer
from .models import Note, Teacher
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


class NoteList(ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['=module__id']
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    serializer_class = NoteSerializer


class NoteCreate(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteRetrieve(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteUpdate(UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteRetUp(RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDestroy(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


@permission_classes((AllowAny,))
class TeacherDetailCreate(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer
