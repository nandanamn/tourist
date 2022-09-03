from urllib import request
from django.shortcuts import render

# Create your views here.


def student_home(request):
    return render(request,'student/home.html')


def student_viewmarks(request):
    return render(request,'student/viewmarks.html')
