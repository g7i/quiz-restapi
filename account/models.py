from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Officer', 'Officer'),
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
