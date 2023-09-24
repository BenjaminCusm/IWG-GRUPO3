from django.shortcuts import render, redirect

# Create your views here.

def prueba(request):
    return render(request,'prueba.html')