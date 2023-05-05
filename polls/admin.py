from django.contrib import admin

from polls.models import Group, Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_filter = ["subject", "first_name"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_filter = ["name"]
