# users/views.py
# from rest_framework.response import Response
# from rest_framework.status import (
#     HTTP_400_BAD_REQUEST,
#     HTTP_404_NOT_FOUND,
#     HTTP_200_OK
# )
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.authtoken.models import Token
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import authenticate
from rest_framework import generics
from .models import School, Hospital, Teacher, Community, Student

from django.contrib.auth import get_user_model
from .serializers import (
    StudentCreateSerializer,
    CommunityRetrieveSerializer,
    BloodBankCreateSerializer,
    HospitalCreateSerializer,
    HospitalRetrieveSerializer,
    ParentCreateSerializer,
    SchoolCreateSerializer,
    CommunityCreateSerializer,
    TeacherCreateSerializer,
    SchoolRetrieveSerializer,
    DriverCreateSerializer,
    HospitalStaffCreateSerializer,
    TeacherSerializer,
    StudentSerializer,
)
User = get_user_model()

# class UserListView(generics.ListAPIView):
#     queryset = models.User.objects.all()
#     serializer_class = serializers.UserSerializer


@permission_classes((AllowAny,))
class StudentCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentCreateSerializer


@permission_classes((AllowAny,))
class StudentList(generics.ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['=school__id']
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@permission_classes((AllowAny,))
class BloodBankCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = BloodBankCreateSerializer


@permission_classes((AllowAny,))
class HospitalCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = HospitalCreateSerializer


@permission_classes((AllowAny,))
class HospitalStaffCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = HospitalStaffCreateSerializer


@permission_classes((AllowAny,))
class HospitalRetrieveView(generics.RetrieveAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalRetrieveSerializer
    lookup_field = 'key'
    # lookup_url_kwarg = 'key'


@permission_classes((AllowAny,))
class ParentCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ParentCreateSerializer


@permission_classes((AllowAny,))
class SchoolCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SchoolCreateSerializer


@permission_classes((AllowAny,))
class SchoolRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = SchoolRetrieveSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'key'


@permission_classes((AllowAny,))
class TeacherCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TeacherCreateSerializer


@permission_classes((AllowAny,))
class CommunityCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CommunityCreateSerializer


@permission_classes((AllowAny,))
class CommunityRetrieveView(generics.RetrieveAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunityRetrieveSerializer
    lookup_field = 'key'


@permission_classes((AllowAny,))
class DriverCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = DriverCreateSerializer


@permission_classes((AllowAny,))
class TeacherList(generics.ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['=school_id__id']
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)
