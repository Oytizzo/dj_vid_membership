from django.shortcuts import render
from django.http import HttpResponse


def courses(request):
    context = {}
    return render(request, 'courses/home.html', context)
