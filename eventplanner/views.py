from django.http import HttpResponse

def aboutUS(request):
    return HttpResponse("Welcome to EG")
def home(request):
    return HttpResponse("<b>THis is home</b>") 
def homeNav(request,name):
    return HttpResponse("<b>Hello</b>   "+name) 