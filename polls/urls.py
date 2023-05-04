from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("teacher/", views.add_teacher, name="add_teacher"),
    path(
        "teacher/edit_delete/<int:id>", views.teacher_edit, name="teacher_edit"
    ),
    path("teachers/", views.teacher_list, name="teachers_display"),
    path("student/", views.add_student, name="add_student"),
    path(
        "student/edit_delete/<int:id>", views.student_edit, name="student_edit"
    ),
    path("students/", views.student_list, name="students_display"),
    path("group/", views.add_group, name="add_group"),
]
