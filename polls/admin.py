from django.contrib import admin

from polls.models import Group, Teacher, Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_filter = ["subject", "first_name"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_filter = ["name"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ordering = ["first_name", "year"]
    list_filter = ["first_name", "year"]
