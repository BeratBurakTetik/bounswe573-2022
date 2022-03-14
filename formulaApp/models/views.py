from django.shortcuts import render
from .models import Circuit
from .models import Constructor

# Create your views here.

def circuit_list(request):
    circuits = Circuit.objects.all()
    return render(request, 'models/circuit_list.html', {'circuits':circuits})

def home(request):
    return render(request, "models/home.html",{})

def constructor_list(request):
    constructors = Constructor.objects.all()
    return render(request, 'models/constructor_list.html',{'constructors':constructors})