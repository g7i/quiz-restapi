from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from .serializers import NoteSerializer
from .models import Note


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
