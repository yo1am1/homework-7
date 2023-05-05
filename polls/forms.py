from django import forms

from .models import Teacher, Group, Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "year"]


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "teacher", "students"]


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "subject"]
