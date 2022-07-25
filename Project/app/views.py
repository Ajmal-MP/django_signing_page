from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login
from .models import Cards
# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            return render(request,'app/login.html',{'message':'Invalid username of password'})
    return render(request,'app/login.html')

@login_required(login_url='login')
def home(request):
    return render(request,'app/home.html',{'cards':Cards.objects.all()})

def logout_page(request):
    if request.method=='POST':
        logout(request)
        return redirect(login_page)
    
