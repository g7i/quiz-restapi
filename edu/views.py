from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from .serializers import NoteSerializer, TeacherDetailSerializer, SchoolActivitySerializer, StudentAddSerializer, FeedbackSerializer, ReportCardSerializer, VideoSerializer, InnovationSerializer
from .models import Note, TeacherDetail, SchoolActivity, Feedback, StudentAdd, ReportCard, Video, Innovation
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


class NoteList(ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['=module__id']
    queryset = Note.objects.all()
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
    queryset = TeacherDetail.objects.all()
    serializer_class = TeacherDetailSerializer


@permission_classes((AllowAny,))
class TeacherDetailView(ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['=teacher__id']
    queryset = TeacherDetail.objects.all()
    serializer_class = TeacherDetailSerializer


@permission_classes((AllowAny,))
class SchoolActivityCreate(CreateAPIView):
    queryset = SchoolActivity.objects.all()
    serializer_class = SchoolActivitySerializer


@permission_classes((AllowAny,))
class SchoolActivityList(ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['=school__id']
    queryset = SchoolActivity.objects.all()
    serializer_class = SchoolActivitySerializer


@permission_classes((AllowAny,))
class StudentAddCreate(CreateAPIView):
    queryset = StudentAdd.objects.all()
    serializer_class = StudentAddSerializer


@permission_classes((AllowAny,))
class StudentAddList(ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['=school__id']
    queryset = StudentAdd.objects.all()
    serializer_class = StudentAddSerializer


@permission_classes((AllowAny,))
class FeedbackCreate(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


@permission_classes((AllowAny,))
class FeedbackList(ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['=teacher__id']
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


@permission_classes((AllowAny,))
class ReportCardCreate(CreateAPIView):
    queryset = ReportCard.objects.all()
    serializer_class = ReportCardSerializer


@permission_classes((AllowAny,))
class ReportCardList(ListAPIView):
    filter_backends = [SearchFilter]
    # search_fields = ['=teacher__id']
    queryset = ReportCard.objects.all()
    serializer_class = ReportCardSerializer


@permission_classes((AllowAny,))
class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


@permission_classes((AllowAny,))
class InnovationCreate(CreateAPIView):
    queryset = Innovation.objects.all()
    serializer_class = InnovationSerializer


@permission_classes((AllowAny,))
class InnovationList(ListAPIView):
    filter_backends = [SearchFilter]
    # search_fields = ['=teacher__id']
    queryset = Innovation.objects.all()
    serializer_class = InnovationSerializer
