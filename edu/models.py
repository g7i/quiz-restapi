from django.db import models
from quizApp.models import Module


class Note(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    doc = models.FileField(upload_to='notes/')
