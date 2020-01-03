# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Student, BloodBank, Hospital, Parent, School, Teacher

User = get_user_model()

admin.site.register(User)
admin.site.register(Student)
admin.site.register(BloodBank)
admin.site.register(Hospital)
admin.site.register(Parent)
admin.site.register(School)
admin.site.register(Teacher)
