from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import TeacherForm, StudentForm, GroupForm
from .models import Teacher, Student, Group


def index(request):
    return HttpResponseRedirect(reverse(home))


def home(request):
    return render(request, "index.html")


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("teacher_edit", args=[form.instance.id])
            )
    else:
        form = TeacherForm()

    context = {"form": form}
    return render(request, "teacher_form.html", context)


def teacher_edit(request, id: int):
    try:
        teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return "There is no teacher with such id!"
    if request.method == "POST":
        if "edit" in request.POST:
            form = TeacherForm(request.POST, instance=teacher)
            if form.is_valid():
                form.save()
                return render(request, "teacher_edit.html", {"form": form})
        elif "delete" in request.POST:
            teacher.delete()
            return HttpResponseRedirect(reverse("teachers_display"))
        elif "display" in request.POST:
            return HttpResponseRedirect(reverse("teachers_display"))
        elif "add" in request.POST:
            return HttpResponseRedirect(reverse("add_teacher"))
    else:
        form = TeacherForm(instance=teacher)
        context = {"form": form}
        return render(request, "teacher_edit.html", context)
    return HttpResponseRedirect(reverse("teacher_edit"))


def teacher_list(request):
    teachers = Teacher.objects.values()
    context = {"teachers": teachers}
    return render(request, "teacher_display.html", context)


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("student_edit", args=[form.instance.id])
            )
    else:
        form = StudentForm()
    context = {"form": form}
    return render(request, "student_form.html", context)


def student_edit(request, id: int):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return "There is no student with such id"
    if request.method == "POST":
        if "edit" in request.POST:
            form = StudentForm(request.POST, instance=student)

            if form.is_valid():
                form.save()
                return render(request, "student_edit.html", {"form": form})
        elif "add" in request.POST:
            return HttpResponseRedirect(reverse("add_student"))
        else:
            student.delete()
            return HttpResponseRedirect(reverse("students_display"))
    else:
        form = StudentForm(instance=student)
        return render(request, "student_edit.html", {"form": form})


def student_list(request):
    students = Student.objects.values()
    context = {"students": students}
    return render(request, "student_display.html", context)


def add_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("add_group"))

    else:
        form = GroupForm()
    context = {"form": form}
    return render(request, "group_form.html", context)


def group_list(request):
    groups = Group.objects.values()
    context = {"groups": groups}
    return render(request, "group_display.html", context)
