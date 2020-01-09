from django.contrib import admin

from .models import (
    HospitalDetail,
    Deptt,
    DoctorDetail,
    Ambulance,
    BloodStock
)

admin.site.register(HospitalDetail)
admin.site.register(Deptt)
admin.site.register(DoctorDetail)
admin.site.register(Ambulance)
admin.site.register(BloodStock)
