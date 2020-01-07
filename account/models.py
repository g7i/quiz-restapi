from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = (
        ('Student', 'Student'),
        ('School', 'School'),
        ('Blood Bank', 'Blood Bank'),
        ('Parent', 'Parent'),
        ('Hospital', 'Hospital'),
        ('Teacher', 'Teacher'),
        ('Community', 'Community'),
        ('Driver', 'Driver'),
        ('Hospital Staff', 'Hospital Staff'),
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
    name = models.CharField(max_length=100)
    tahsil = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField()
    address = models.TextField()
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)

    def __str__(self):
        return self.user.username


class Hospital(models.Model):
    tahsil = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=50, unique=True, null=True)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField()
    region = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)

    def __str__(self):
        return self.user.username


class Parent(models.Model):
    state = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField()
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class School(models.Model):
    board = models.CharField(max_length=100)
    address = models.TextField()
    mobile_number = models.BigIntegerField()
    state = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    address = models.TextField()
    mobile_number = models.BigIntegerField()
    state = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Community(models.Model):
    service = models.CharField(max_length=100)
    amb_number = models.CharField(max_length=50)
    key = models.CharField(max_length=50, unique=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    district = models.CharField(max_length=50)
    address = models.TextField()
    mobile_number = models.BigIntegerField()
    state = models.CharField(max_length=50)
    org_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Driver(models.Model):
    dl_number = models.CharField(max_length=50)
    driving_exp = models.DecimalField(max_digits=15, decimal_places=2)
    age = models.IntegerField()
    photo = models.FileField(upload_to='drivers/')
    com_id = models.ForeignKey(Community, on_delete=models.CASCADE)
    mobile_number = models.BigIntegerField()
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class HospitalStaff(models.Model):

    TYPE = (
        ('ward', 'ward'),
        ('lab', 'lab')
    )

    hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=100)
    mobile_number = models.BigIntegerField()
    state = models.CharField(max_length=50)
    tahseel = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_type = models.CharField(max_length=10, choices=TYPE)

    def __str__(self):
        return self.user.username
