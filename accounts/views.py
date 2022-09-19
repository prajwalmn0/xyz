from threading import activeCount
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect

# Create your views here.
def signup(request):
    if request.method=="POST":
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        username=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
        print('account created')
        return redirect('/accounts/login')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            print('you are logged in')
            return redirect('/navbar/home')
    else:
        return render(request,'login.html')

def account(request):
    return render(request,'account.html')

