from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Student, BloodBank, Hospital, Parent, School, Teacher, Community, Driver, HospitalStaff, Industry
User = get_user_model()


class StudentCreateSerializer(serializers.ModelSerializer):
    father_name = serializers.CharField(label='father_name')
    father_aadhar = serializers.IntegerField(label='father_aadhar')
    aadhar = serializers.IntegerField(label='aadhar')
    mobile_number = serializers.IntegerField(label='mobile_number')
    school_id = serializers.IntegerField(label='school_id')
    address = serializers.CharField(label='address')
    state = serializers.CharField(label='state')

    class Meta:
        model = User
        fields = [
            'aadhar',
            'password',
            'email',
            'first_name',
            'father_name',
            'father_aadhar',
            'mobile_number',
            'address',
            'state',
            'school_id'
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['aadhar']
        email = validated_data['email']
        first_name = validated_data['first_name']
        password = validated_data['password']
        father_name = validated_data['father_name']
        father_aadhar = validated_data['father_aadhar']
        mobile_number = validated_data['mobile_number']
        address = validated_data['address']
        state = validated_data['state']
        school_id = validated_data['school_id']
        user_obj = User.objects.create_user(
            username=username,
            email=email,
            user_type="Student",
            password=password,
            first_name=first_name
        )
        Student.objects.create(
            father_name=father_name,
            father_aadhar=father_aadhar,
            mobile_number=mobile_number,
            address=address,
            state=state,
            user=user_obj,
            school_id=School.objects.get(pk=school_id)
        )
        return validated_data

###############################################################################


class BloodBankCreateSerializer(serializers.ModelSerializer):
    tahsil = serializers.CharField(label='tahsil')
    mobile_number = serializers.IntegerField(label='mobile_number')
    aadhar = serializers.IntegerField(label='aadhar')
    address = serializers.CharField(label='address')
    region = serializers.CharField(label='region')
    latitude = serializers.DecimalField(
        label='latitude', max_digits=15, decimal_places=10)
    longitude = serializers.DecimalField(
        label='longitude', max_digits=15, decimal_places=10)
    state = serializers.CharField(label='state')
    district = serializers.CharField(label='district')
    name = serializers.CharField(label='name')

    class Meta:
        model = User
        fields = [
            'aadhar',
            'password',
            'email',
            'first_name',
            'tahsil',
            'latitude',
            'longitude',
            'mobile_number',
            'address',
            'region',
            'state',
            'district',
            'name'
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['aadhar']
        email = validated_data['email']
        first_name = validated_data['first_name']
        password = validated_data['password']
        tahsil = validated_data['tahsil']
        latitude = validated_data['latitude']
        longitude = validated_data['longitude']
        address = validated_data['address']
        mobile_number = validated_data['mobile_number']
        region = validated_data['region']
        state = validated_data['state']
        district = validated_data['district']
        name = validated_data['name']
        user_obj = User.objects.create_user(
            username=username,
            email=email,
            user_type="Blood Bank",
            password=password,
            first_name=first_name
        )
        BloodBank.objects.create(
            tahsil=tahsil,
            mobile_number=mobile_number,
            address=address,
            region=region,
            latitude=latitude,
            longitude=longitude,
            user=user_obj,
            state=state,
            district=district,
            name=name
        )
        return validated_data

###############################################################################


class HospitalCreateSerializer(serializers.ModelSerializer):
    tahsil = serializers.CharField(label='tahsil')
    state = serializers.CharField(label='state')
    key = serializers.CharField(label='key')
    district = serializers.CharField(label='district')
    name = serializers.CharField(label='name')
    mobile_number = serializers.IntegerField(label='mobile_number')
    aadhar = serializers.IntegerField(label='aadhar')
    region = serializers.CharField(label='region')
    latitude = serializers.DecimalField(
        label='latitude', max_digits=15, decimal_places=10)
    longitude = serializers.DecimalField(
        label='longitude', max_digits=15, decimal_places=10)

    class Meta:
        model = User
        fields = [
            'aadhar',
            'password',
            'email',
            'first_name',
            'tahsil',
            'key',
            'latitude',
            'longitude',
            'mobile_number',
            'region',
            'state',
            'district',
            'name'
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['aadhar']
        email = validated_data['email']
        first_name = validated_data['first_name']
        password = validated_data['password']
        key = validated_data['key']
        tahsil = validated_data['tahsil']
        latitude = validated_data['latitude']
        longitude = validated_data['longitude']
        mobile_number = validated_data['mobile_number']
        region = validated_data['region']
        state = validated_data['state']
        district = validated_data['district']
        name = validated_data['name']
        user_obj = User.objects.create_user(
            username=username,
            email=email,
            user_type="Hospital",
            password=password,
            first_name=first_name
        )
        Hospital.objects.create(
            tahsil=tahsil,
            mobile_number=mobile_number,
            region=region,
            latitude=latitude,
            longitude=longitude,
            key=key,
            state=state,
            district=district,
            name=name,
            user=user_obj
        )
        return validated_data


###############################################################################


class HospitalStaffCreateSerializer(serializers.ModelSerializer):
    TYPE = (
        ('ward', 'ward'),
        ('lab', 'lab')
    )
    tahseel = serializers.CharField(label='tahseel')
    staff_type = serializers.ChoiceField(label='staff_type', choices=TYPE)
    state = serializers.CharField(label='state')
    hospital_id = serializers.CharField(label='hospital_id')
    district = serializers.CharField(label='district')
    hospital_name = serializers.CharField(label='hospital_name')
    mobile_number = serializers.IntegerField(label='mobile_number')
    aadhar = serializers.IntegerField(label='aadhar')
    region = serializers.CharField(label='region')
    village = serializers.CharField(label='village')
    latitude = serializers.DecimalField(
        label='latitude', max_digits=15, decimal_places=10)
    longitude = serializers.DecimalField(
        label='longitude', max_digits=15, decimal_places=10)

    class Meta:
        model = User
        fields = [
            'aadhar',
            'staff_type',
            'password',
            'email',
            'first_name',
            'tahseel',
            'hospital_id',
            'latitude',
            'longitude',
            'mobile_number',
            'region',
            'hospital_name',
            'village',
            'state',
            'district',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['aadhar']
        email = validated_data['email']
        first_name = validated_data['first_name']
        password = validated_data['password']
        hospital_id = validated_data['hospital_id']
        tahseel = validated_data['tahseel']
        latitude = validated_data['latitude']
        longitude = validated_data['longitude']
        mobile_number = validated_data['mobile_number']
        region = validated_data['region']
        state = validated_data['state']
        district = validated_data['district']
        village = validated_data['village']
        hospital_name = validated_data['hospital_name']
        staff_type = validated_data['staff_type']
        user_obj = User.objects.create_user(
            username=username,
            email=email,
            user_type="Hospital Staff",
            password=password,
            first_name=first_name
        )
        HospitalStaff.objects.create(
            tahseel=tahseel,
            mobile_number=mobile_number,
            region=region,
            latitude=latitude,
            longitude=longitude,
            hospital_id=get_object_or_404(Hospital, pk=hospital_id),
            state=state,
            district=district,
            village=village,
            hospital_name=hospital_name,
            staff_type=staff_type,
            user=user_obj
        )
        return validated_data

############################################################################################


class HospitalRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = [
            'id',
            'name'
        ]


###############################################################################


class ParentCreateSerializer(serializers.ModelSerializer):
    state = serializers.CharField(label='state')
    address = serializers.CharField(label='address')
    mobile_number = serializers.IntegerField(label='mobile_number')
    aadhar = serializers.IntegerField(label='aadhar')

    class Meta:
        model = User
        fields = [
            'aadhar',
            'password',
            'email',
            'first_name',
            'mobile_number',
            'address',
            'state',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['aadhar']
        email = validated_data['email']
        first_name = validated_data['first_name']
        password = validated_data['password']
        mobile_number = validated_data['mobile_number']
        address = validated_data['address']
        state = validated_data['state']
        user_obj = User.objects.create_user(
            username=username,
            email=email,
            user_type="Parent",
            password=password,
            first_name=first_name
        )
        Parent.objects.create(
            mobile_number=mobile_number,
            address=address,
            state=state,
            user=user_obj
        )
        return validated_data

###############################################################################


class SchoolCreateSerializer(serializers.ModelSerializer):
    state = serializers.CharField(label='state')
    address = serializers.CharField(label='address')
    mobile_number = serializers.IntegerField(label='mobile_number')
    key = serializers.CharField(label='key')
    board = serializers.CharField(label='board')

    class Meta:
        model = User
        fields = [
            'key',
            'password',
            'email',
            'first_name',
            'mobile_number',
            'address',
            'state',
            'board',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['key']
        email = validated_data['email']
        first_name = validated_data['first_name']
        password = validated_data['password']
        mobile_number = validated_data['mobile_number']
        address = validated_data['address']
        state = validated_data['state']
        board = validated_data['board']
        user_obj = User.objects.create_user(
            username=username,
            email=email,
            user_type="School",
            password=password,
            first_name=first_name
        )
        School.objects.create(
            mobile_number=mobile_number,
            address=address,
            state=state,
            board=board,
            user=user_obj
        )
        return validated_data

###############################################################################


class TeacherCreateSerializer(serializers.ModelSerializer):
    state = serializers.CharField(label='state')
    address = serializers.CharField(label='address')
    mobile_number = serializers.IntegerField(label='mobile_number')
    aadhar = serializers.IntegerField(label='aadhar')
    school_id = serializers.IntegerField(label='school_id')

    class Meta:
        model = User
        fields = [
            'aadhar',
            'password',
            'email',
            'first_name',
            'mobile_number',
            'address',
            'state',
            'school_id'
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['aadhar']
        email = validated_data['email']
        first_name = validated_data['first_name']
        password = validated_data['password']
        mobile_number = validated_data['mobile_number']
        address = validated_data['address']
        state = validated_data['state']
        school_id = validated_data['school_id']
        user_obj = User.objects.create_user(
            username=username,
            email=email,
            user_type="Teacher",
            password=password,
            first_name=first_name
        )
        Teacher.objects.create(
            mobile_number=mobile_number,
            address=address,
            state=state,
            school_id=get_object_or_404(School, pk=school_id),
            user=user_obj
        )
        return validated_data

############################################################################################


class SchoolRetrieveSerializer(serializers.ModelSerializer):
    school_id = serializers.IntegerField(label="school_id", source="school.id")

    class Meta:
        model = User
        fields = [
            'school_id',
            'first_name'
        ]


###############################################################################


class CommunityCreateSerializer(serializers.ModelSerializer):
    service = serializers.CharField(label="service")
    aadhar = serializers.CharField(label="aadhar")
    amb_number = serializers.CharField(label="amb_number")
    latitude = serializers.DecimalField(
        max_digits=15, decimal_places=10, label="latitude")
    longitude = serializers.DecimalField(
        max_digits=15, decimal_places=10, label="longitude")
    district = serializers.CharField(label="district")
    address = serializers.CharField(label="address")
    mobile_number = serializers.IntegerField(label="mobile_number")
    state = serializers.CharField(label="state")
    org_name = serializers.CharField(label="org_name")
    key = serializers.CharField(label="key")

    class Meta:
        model = User
        fields = [
            'aadhar',
            'password',
            'first_name',
            'service',
            'amb_number',
            'latitude',
            'longitude',
            'district',
            'address',
            'mobile_number',
            'state',
            'org_name',
            'key',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['aadhar']
        service = validated_data['service']
        first_name = validated_data['first_name']
        password = validated_data['password']
        amb_number = validated_data['amb_number']
        longitude = validated_data['longitude']
        latitude = validated_data['latitude']
        district = validated_data['district']
        mobile_number = validated_data['mobile_number']
        address = validated_data['address']
        state = validated_data['state']
        key = validated_data['key']
        org_name = validated_data['org_name']
        user_obj = User.objects.create_user(
            username=username,
            user_type="Community",
            password=password,
            first_name=first_name
        )
        Community.objects.create(
            mobile_number=mobile_number,
            address=address,
            state=state,
            key=key,
            service=service,
            amb_number=amb_number,
            longitude=longitude,
            latitude=latitude,
            district=district,
            org_name=org_name,
            user=user_obj
        )
        return validated_data


############################################################################################


class CommunityRetrieveSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label="name", source="user.first_name")

    class Meta:
        model = Community
        fields = [
            'id',
            'name'
        ]


###############################################################################


class DriverCreateSerializer(serializers.ModelSerializer):
    aadhar = serializers.CharField(label="aadhar")
    dl_number = serializers.CharField(label='dl_number')
    driving_exp = serializers.DecimalField(
        max_digits=15, decimal_places=2, label='driving_exp')
    age = serializers.IntegerField(label='age')
    com_id = serializers.IntegerField(label='com_id')
    photo = serializers.FileField(label='photo')
    mobile_number = serializers.IntegerField(label='mobile_number')
    state = serializers.CharField(label='state')
    district = serializers.CharField(label='district')

    class Meta:
        model = User
        fields = [
            'aadhar',
            'password',
            'first_name',
            'email',
            'com_id',
            'dl_number',
            'driving_exp',
            'age',
            'photo',
            'mobile_number',
            'state',
            'district',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['aadhar']
        first_name = validated_data['first_name']
        password = validated_data['password']
        email = validated_data['email']
        dl_number = validated_data['dl_number']
        driving_exp = validated_data['driving_exp']
        age = validated_data['age']
        mobile_number = validated_data['mobile_number']
        photo = validated_data['photo']
        com_id = validated_data['com_id']
        state = validated_data['state']
        district = validated_data['district']
        user_obj = User.objects.create_user(
            username=username,
            user_type="Driver",
            password=password,
            first_name=first_name,
            email=email
        )
        Driver.objects.create(
            dl_number=dl_number,
            driving_exp=driving_exp,
            age=age,
            mobile_number=mobile_number,
            photo=photo,
            state=state,
            com_id=get_object_or_404(Community, pk=com_id),
            district=district,
            user=user_obj
        )
        return validated_data


###########################################################################

class TeacherSerializer(serializers.ModelSerializer):
    aadhar = serializers.IntegerField(label="aadhar", source="user.username")
    name = serializers.CharField(label="name", source="user.first_name")
    email = serializers.CharField(label="email", source="user.email")

    class Meta:
        model = Teacher
        fields = "__all__"

############################################################################


class StudentSerializer(serializers.ModelSerializer):
    aadhar = serializers.IntegerField(label="aadhar", source="user.username")
    name = serializers.CharField(label="name", source="user.first_name")
    email = serializers.CharField(label="email", source="user.email")

    class Meta:
        model = Student
        fields = "__all__"


###############################################################################


class IndustryCreateSerializer(serializers.ModelSerializer):
    tan = serializers.CharField(label="tan")
    gst = serializers.CharField(label="gst")
    opt_name = serializers.CharField(label="opt_name")
    desig = serializers.CharField(label="desig")
    mobile_number = serializers.IntegerField(label="mobile_number")
    address = serializers.CharField(label="address")
    teh = serializers.CharField(label="teh")
    district = serializers.CharField(label="district")
    state = serializers.CharField(label="state")
    pincode = serializers.IntegerField(label="pincode")
    industry_name = serializers.CharField(label="industry_name")
    reg_num = serializers.CharField(label="reg_name")

    class Meta:
        model = User
        fields = [
            'industry_name',
            'reg_num',
            'opt_name',
            'email',
            'password',
            'tan',
            'gst',
            'desig',
            'address',
            'mobile_number',
            'state',
            'teh',
            'district',
            'pincode',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['reg_num']
        email = validated_data['email']
        first_name = validated_data['industry_name']
        password = validated_data['password']
        opt_name = validated_data['opt_name']
        tan = validated_data['tan']
        gst = validated_data['gst']
        desig = validated_data['desig']
        mobile_number = validated_data['mobile_number']
        address = validated_data['address']
        state = validated_data['state']
        teh = validated_data['teh']
        district = validated_data['district']
        pincode = validated_data['pincode']
        user_obj = User.objects.create_user(
            username=username,
            user_type="Industry",
            password=password,
            first_name=first_name,
            email=email
        )
        Industry.objects.create(
            opt_name=opt_name,
            tan=tan,
            gst=gst,
            desig=desig,
            mobile_number=mobile_number,
            address=address,
            state=state,
            teh=teh,
            district=district,
            pincode=pincode,
            user=user_obj
        )
        return validated_data
