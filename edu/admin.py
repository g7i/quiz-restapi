from django.contrib import admin
from .models import Note, TeacherDetail, SchoolActivity, Feedback, StudentAdd, ReportCard, Video

admin.site.register(Note)
admin.site.register(SchoolActivity)
admin.site.register(TeacherDetail)
admin.site.register(Feedback)
admin.site.register(StudentAdd)
admin.site.register(Video)
admin.site.register(ReportCard)
