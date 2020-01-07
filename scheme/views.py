from rest_framework.generics import (
    ListAPIView,
)
from .models import Scheme
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import SchemeSerializer


@permission_classes((AllowAny,))
class SchemeSerializerView(ListAPIView):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer
