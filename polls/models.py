from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    year = models.IntegerField(default=1)
    group = models.CharField(max_length=50)


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)


class Group(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    students = models.ManyToManyField(Student, related_name="student_groups")
