from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html",{})

def aboutus(request):
    return render(request,"aboutus.html",{})

def courses(request):
    return render(request,"courses.html",{})

def ourservices(request):
    return render(request,"ourservices.html",{})

def ourachievers(request):
    return render(request,"ourachievers.html",{})

def gallery(request):
    return render(request,"gallery.html",{})

def contactus(request):
    return render(request,"contactus.html",{})