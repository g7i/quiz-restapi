from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Officer', 'Officer'),
    )

    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.CharField(
        max_length=20, choices=USER, blank=True, null=True)

    # @property
    # def age(self):
    #     try:
    #         return int(round((datetime.now().date() - self.dob).days / 365.25))
    #     except:
    #         return '-'

    def __str__(self):
        return self.username
