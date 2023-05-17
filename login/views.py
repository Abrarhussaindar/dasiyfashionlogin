from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *

# Create your views here.
def login(request):
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        password = request.POST.get('Password')
        # print(roll_number, password)
        student = authenticate(request, roll_number=roll_number, password=password)
    # print(student.is_authenticated)
        if student is not None:
            login(request, student)
            return redirect('home')
    context = {}
    return render(request, "login.html", context)