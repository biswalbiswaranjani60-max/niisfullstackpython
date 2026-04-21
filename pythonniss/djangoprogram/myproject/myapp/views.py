from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    


def home1(request):
	return HttpResponse("Hello World")

def about1(request):
	return HttpResponse("About Page")

def contact(request):
	return HttpResponse("Contact Page")

def services(request):
	return HttpResponse("Our services")

def welcome(request, name):
	return HttpResponse(f"Welcome {name}!")