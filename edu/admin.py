from django.contrib import admin
from .models import Note, TeacherDetail, SchoolActivity

admin.site.register(Note)
admin.site.register(SchoolActivity)
admin.site.register(TeacherDetail)
