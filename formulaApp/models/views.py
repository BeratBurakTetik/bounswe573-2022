from urllib import request
from django.shortcuts import render
from .models import Circuit
from .models import Constructor
from .models import Driver

# Create your views here.

def circuit_list(request):
    circuits = Circuit.objects.all()
    return render(request, 'models/circuit_list.html', {'circuits':circuits})

def home(request):
    return render(request, "models/home.html",{})

def constructor_list(request):
    constructors = Constructor.objects.all()
    return render(request, 'models/constructor_list.html',{'constructors':constructors})

def driver_list(request):
    drivers = Driver.objects.all()
    return render(request,'models/driver_list.html',{'drivers':drivers})