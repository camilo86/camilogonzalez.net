from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {})

def contactMe(request):
    return render(request, 'contactMe.html', {})

def aboutMe(request):
    return render(request, 'aboutMe.html', {})
