from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def service(request):
    return render(request,"service.html")

def project(request):
    return render(request,"project.html")