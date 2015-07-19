from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Rango sais Heloooo! <a href="/rango/about">About</a>')
    
    
def about (request):
    return HttpResponse('Rango says here is the about page. <a href="/rango">Home</a>')