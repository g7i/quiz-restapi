from rest_framework.serializers import ModelSerializer

from .models import Subject,Class,Topic,Module,Question,Choice,Score

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class ModuleSerializer(ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'

class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'