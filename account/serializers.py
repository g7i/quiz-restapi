from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Student, BloodBank
User = get_user_model()


class StudentCreateSerializer(serializers.ModelSerializer):
    father_name = serializers.CharField(label='father_name')
    father_aadhar = serializers.IntegerField(label='father_aadhar')
    mobile_number = serializers.IntegerField(label='mobile_number')
    address = serializers.CharField(label='address')
    state = serializers.CharField(label='state')

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'father_name',
            'father_aadhar',
            'mobile_number',
            'address',
            'state'
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        first_name = validated_data['first_name']
        password = validated_data['password']
        father_name = validated_data['father_name']
        father_aadhar = validated_data['father_aadhar']
        mobile_number = validated_data['mobile_number']
        address = validated_data['address']
        state = validated_data['state']
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
            user=user_obj
        )
        return validated_data

###############################################################################


class BloodBankCreateSerializer(serializers.ModelSerializer):
    tahsil = serializers.CharField(label='tahsil')
    mobile_number = serializers.IntegerField(label='mobile_number')
    address = serializers.CharField(label='address')
    region = serializers.CharField(label='region')
    latitude = serializers.DecimalField(
        label='latitude', max_digits=15, decimal_places=10)
    longitude = serializers.DecimalField(
        label='longitude', max_digits=15, decimal_places=10)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'tahsil',
            'latitude',
            'longitude',
            'mobile_number',
            'address',
            'region'
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        first_name = validated_data['first_name']
        password = validated_data['password']
        tahsil = validated_data['tahsil']
        latitude = validated_data['latitude']
        longitude = validated_data['longitude']
        address = validated_data['address']
        mobile_number = validated_data['mobile_number']
        region = validated_data['region']
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
            user=user_obj
        )
        return validated_data
