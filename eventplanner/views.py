from django.http import HttpResponse
from django.shortcuts import render
def aboutUS(request):
    return HttpResponse("Welcome to EG")
def home(request):
    return render(request,"index.html") 
def homeNav(request,name):
    return HttpResponse("<b>Hello</b>   "+name) 
def about(request):
    return HttpResponse("hi this is features")
def login(request):
    return render(request,"login.html") 
def signup(request):
    return render(request,"signup.html") 