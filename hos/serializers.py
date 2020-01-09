from rest_framework.serializers import ModelSerializer
from .models import (
    HospitalDetail,
    Deptt,
    DoctorDetail,
    Ambulance,
    BloodStock
)


class HospitalDetailSerializer(ModelSerializer):
    class Meta:
        model = HospitalDetail
        fields = '__all__'


class DepttSerializer(ModelSerializer):
    class Meta:
        model = Deptt
        fields = "__all__"


class DoctorDetailSerializer(ModelSerializer):
    class Meta:
        model = DoctorDetail
        fields = "__all__"


class AmbulanceSerializer(ModelSerializer):
    class Meta:
        model = Ambulance
        fields = "__all__"


class BloodStockSerializer(ModelSerializer):
    class Meta:
        model = BloodStock
        fields = "__all__"
