from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    studens = Student.objects.prefetch_related('teacher').order_by('group').all()
    context = {'object_list': studens}

    return render(request, template, context)
