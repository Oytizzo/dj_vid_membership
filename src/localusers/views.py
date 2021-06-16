from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello world!</h1>")
