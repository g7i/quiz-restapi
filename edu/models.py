from django.db import models
from quizApp.models import Module, Class, Subject
from account.models import Teacher, School, Parent, Student, School


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


class StudentAdd(models.Model):
    clas = models.ForeignKey(Class, on_delete=models.CASCADE)
    stream = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    aadhar = models.BigIntegerField()


class Feedback(models.Model):
    teacher_id = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, null=True, blank=True)
    student_id = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True)
    parent_id = models.ForeignKey(
        Parent, on_delete=models.CASCADE, null=True, blank=True)
    school_id = models.ForeignKey(
        School, on_delete=models.CASCADE, null=True, blank=True)
    field1 = models.BooleanField()
    field2 = models.BooleanField()
    field3 = models.BooleanField()
    field4 = models.BooleanField()
    field5 = models.BooleanField()
    field6 = models.BooleanField()
    field7 = models.BooleanField()
    field8 = models.BooleanField()
    field9 = models.BooleanField()
    field10 = models.BooleanField()


class ReportCard(models.Model):
    name = models.CharField(max_length=50)
    aadhar = models.BigIntegerField()
    clas = models.CharField(max_length=10)
    subject = models.CharField(max_length=30)
    teacher_name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    validity = models.CharField(max_length=50)
    total_classes = models.IntegerField()
    attended_classes = models.IntegerField()
    exam_name = models.CharField(max_length=50)
    marks = models.IntegerField()
    homework_number = models.IntegerField()
    learning = models.BooleanField()
    behaviour = models.CharField(max_length=50)
    sports = models.CharField(max_length=50)
    extra_act = models.CharField(max_length=50)
    moral_edu = models.CharField(max_length=50)
    concentration = models.CharField(max_length=50)
    suggestions = models.TextField()


class Video(models.Model):
    type = models.CharField(max_length=50)
    select = models.CharField(max_length=50)
    clas = models.CharField(max_length=20)
    image = models.ImageField()
    video = models.FileField(upload_to='videos/')
    doc = models.FileField(upload_to='docV/')
