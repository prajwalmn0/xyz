from http.client import HTTPResponse
from re import X
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    x=30
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')