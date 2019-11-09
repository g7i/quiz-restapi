from django.contrib import admin
from .models import Subject,Class,Topic,Module,Question,Choice,Score

admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Topic)
admin.site.register(Module)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Score)