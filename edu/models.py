from django.db import models
from quizApp.models import Module


class Note(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    doc = models.FileField(upload_to='notes/')
