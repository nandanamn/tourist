from nturl2path import url2pathname
from django import views
from django.urls import path
from .import views



urlpatterns = [
    path('home',views.student_home),
   
    path('contact',views.student_contact),
    path('ampalappuzha',views.student_ampalappuzha),
    path('daytrip',views.student_daytrip),
    path('coirmuseum',views.student_coirmuseum),
    path('alappuzha',views.student_alappuzha),
    
    path('mararibeach',views.student_mararibeach),
    path('lighthouse',views.student_lighthouse),
    path('about',views.student_about),
    path('allplace',views.student_allplace)



]