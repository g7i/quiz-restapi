from django.db import models
from quizApp.models import Module, Class, Subject
from account.models import Teacher, School


class Note(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    doc = models.FileField(upload_to='notes/')

    def __str__(self):
        return self.module.title


class TeacherDetail(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    clas = models.ForeignKey(Class, on_delete=models.CASCADE)
    stream = models.CharField(max_length=50, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    batch = models.CharField(max_length=20)

    def __str__(self):
        return self.teacher.user.first_name + " : " + self.clas.std


class SchoolActivity(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    notice = models.TextField()
    venue = models.TextField()
    teacher = models.TextField()
    student = models.TextField()
