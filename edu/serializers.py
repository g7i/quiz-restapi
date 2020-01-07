from rest_framework.serializers import ModelSerializer
from .models import Note, TeacherDetail, SchoolActivity


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
