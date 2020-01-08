from rest_framework.serializers import ModelSerializer
from .models import Note, TeacherDetail, SchoolActivity, StudentAdd, Feedback, ReportCard


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class TeacherDetailSerializer(ModelSerializer):
    class Meta:
        model = TeacherDetail
        fields = "__all__"


class SchoolActivitySerializer(ModelSerializer):
    class Meta:
        model = SchoolActivity
        fields = "__all__"


class StudentAddSerializer(ModelSerializer):
    class Meta:
        model = StudentAdd
        fields = "__all__"


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"


class ReportCardSerializer(ModelSerializer):
    class Meta:
        model = ReportCard
        fields = "__all__"
