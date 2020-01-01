from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Student
User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    father_name = serializers.CharField(label='father_name')
    father_aadhar = serializers.IntegerField(label='father_name')
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
            'user_type',
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
        user_type = validated_data['user_type']
        user_obj = User.objects.create_user(
            username=username,
            email=email,
            user_type=user_type,
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
