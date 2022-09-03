from django.test import TestCase

# Create your tests here.
def student_home(request):
    return render(request,'student/home.html')