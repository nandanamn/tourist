from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('home',views.student_home,name="home"),
    path('viewmarks',views.student_viewmarks,name="viewmarks")
   
]