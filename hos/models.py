from django.db import models


class HospitalDetail(models.Model):
    cat = models.CharField(max_length=50)
    org = models.CharField(max_length=50)
    madicalFacility = models.BooleanField()
    bloodFacility = models.BooleanField()


class Deptt(models.Model):

    TYPE = (
        ('department', 'department'),
        ('teeka', 'teeka'),
        ('medicine', 'medicine'),
        ('ward detail', 'ward detail'),
        ('ambulance', 'ambulance'),
    )

    field1 = models.BooleanField()
    field2 = models.BooleanField()
    field3 = models.BooleanField()
    field4 = models.BooleanField()
    field5 = models.BooleanField()
    type = models.CharField(max_length=20, choices=TYPE)


class DoctorDetail(models.Model):
    name = models.CharField(max_length=50)
    org = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    aadhar = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    spec = models.TextField()
    address = models.TextField()
    state = models.CharField(max_length=50)
    distric = models.CharField(max_length=50)
    pincode = models.IntegerField()


class Ambulance(models.Model):
    type = models.CharField(max_length=50)
    hospital_linked = models.BooleanField()
    service = models.CharField(max_length=50)
    vehicle = models.CharField(max_length=20)
    model = models.CharField(max_length=50)


class BloodStock(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()
    total = models.IntegerField()
    bGroup = models.CharField(max_length=10)
    amt = models.IntegerField()
    unit = models.IntegerField()
