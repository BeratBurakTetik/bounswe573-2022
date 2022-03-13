from django.shortcuts import render

# Create your views here.

def circuit_list(request):
    return render(request, 'models/circuit_list.html', {})