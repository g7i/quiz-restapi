from rest_framework.serializers import ModelSerializer

from .models import Scheme, CSR


class SchemeSerializer(ModelSerializer):
    class Meta:
        model = Scheme
        fields = "__all__"


class CSRSerializer(ModelSerializer):
    class Meta:
        model = CSR
        fields = "__all__"
