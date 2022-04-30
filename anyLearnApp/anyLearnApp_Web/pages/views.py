from curses.ascii import HT
from django.shortcuts import render

def index(request):
    return render(request,'index.html')