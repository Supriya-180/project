from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,"home.html")

def service(request):
    return render(request,"services.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def component(request):
    return render(request,"components.html")

def project(request):
    return render(request,"project.html")

