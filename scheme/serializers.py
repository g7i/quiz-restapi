from rest_framework.serializers import ModelSerializer

from .models import Scheme


class SchemeSerializer(ModelSerializer):
    class Meta:
        model = Scheme
        fields = "__all__"
