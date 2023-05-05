from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    year = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.first_name} ({self.year} year)"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} ({self.subject})"


class Group(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
