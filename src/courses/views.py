from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from .models import Course, Lesson


def courses(request):
    context = {}
    return render(request, 'courses/home.html', context)


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course
