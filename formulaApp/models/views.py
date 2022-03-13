from django.shortcuts import render
from .models import Circuit

# Create your views here.

def circuit_list(request):
    circuits = Circuit.objects.all()
    return render(request, 'models/circuit_list.html', {'circuits':circuits})