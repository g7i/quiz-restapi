from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import (
    HospitalDetail,
    Deptt,
    DoctorDetail,
    Ambulance,
    BloodStock
)
from .serializers import (
    HospitalDetailSerializer,
    DepttSerializer,
    DoctorDetailSerializer,
    AmbulanceSerializer,
    BloodStockSerializer
)
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


@permission_classes((AllowAny,))
class HospitalDetailList(ListAPIView):
    queryset = HospitalDetail.objects.all()
    serializer_class = HospitalDetailSerializer


@permission_classes((AllowAny,))
class HospitalDetailCreate(CreateAPIView):
    serializer_class = HospitalDetailSerializer


@permission_classes((AllowAny,))
class DepttList(ListAPIView):
    queryset = Deptt.objects.all()
    serializer_class = DepttSerializer


@permission_classes((AllowAny,))
class DepttCreate(CreateAPIView):
    serializer_class = DepttSerializer


@permission_classes((AllowAny,))
class DoctorDetailList(ListAPIView):
    queryset = DoctorDetail.objects.all()
    serializer_class = DoctorDetailSerializer


@permission_classes((AllowAny,))
class DoctorDetailCreate(CreateAPIView):
    serializer_class = DoctorDetailSerializer


@permission_classes((AllowAny,))
class AmbulanceList(ListAPIView):
    queryset = Ambulance.objects.all()
    serializer_class = AmbulanceSerializer


@permission_classes((AllowAny,))
class AmbulanceCreate(CreateAPIView):
    serializer_class = AmbulanceSerializer


@permission_classes((AllowAny,))
class BloodStockList(ListAPIView):
    queryset = BloodStock.objects.all()
    serializer_class = BloodStockSerializer


@permission_classes((AllowAny,))
class BloodStockCreate(CreateAPIView):
    serializer_class = BloodStockSerializer
