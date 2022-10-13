from urllib import request
from django.shortcuts import render

# Create your views here.

def student_home(request):
        return render(request,'student/home.html')

def student_contact(request):
        return render(request,'student/contact.html')
def student_ampalappuzha(request):
        return render(request,'student/ampalappuzha.html')


def student_daytrip(request):
        return render(request,'student/daytrip.html')
       

def student_coirmuseum(request):
        return render(request,'student/coirmuseum.html')
          

def student_alappuzha(request):
        return render(request,'student/alappuzha.html')

 
def student_mararibeach(request):
        return render(request,'student/mararibeach.html')   

def student_lighthouse(request):
        return render(request,'student/lighthouse.html')   


def student_about(request):
        return render(request,'student/about.html')   


 
def student_allplace(request):
        return render(request,'student/allplace.html')   
            
         
    
    




