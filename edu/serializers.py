from rest_framework.serializers import ModelSerializer
from .models import Note, TeacherDetail


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class TeacherDetailSerializer(ModelSerializer):
    class Meta:
        model = TeacherDetail
        fields = "__all__"
