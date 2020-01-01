from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Officer', 'Officer'),
        ('Blood Bank', 'Blood Bank'),
    )

    user_type = models.CharField(
        max_length=20, choices=USER, blank=True, null=True)

    def __str__(self):
        return self.username


class Student(models.Model):
    father_name = models.CharField(max_length=50)
    father_aadhar = models.BigIntegerField()
    mobile_number = models.BigIntegerField()
    address = models.TextField()
    state = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class BloodBank(models.Model):
    tahsil = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField()
    address = models.TextField()
    region = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)

    def __str__(self):
        return self.user.username
