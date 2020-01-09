from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from .models import Scheme, CSR
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import SchemeSerializer, CSRSerializer


@permission_classes((AllowAny,))
class SchemeSerializerView(ListAPIView):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer


@permission_classes((AllowAny,))
class CSRList(ListAPIView):
    queryset = CSR.objects.all()
    serializer_class = CSRSerializer


@permission_classes((AllowAny,))
class CSRCreate(CreateAPIView):
    queryset = CSR.objects.all()
    serializer_class = CSRSerializer
