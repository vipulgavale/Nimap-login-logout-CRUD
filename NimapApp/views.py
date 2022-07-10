from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from NimapApp.forms import MyNimapInfo,ClientInfoForm,ClientUserInfoForm
from django.contrib import messages
# Create your views here.

def client_registration(request):
    form = ClientUserInfoForm()

    if request.method == "POST":

        form= ClientUserInfoForm(request.POST)
        
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"You login successfully with"+user)
        return redirect('')

    context= {'form':form}
    return render(request,'NimapApp/registration.html',context)

def client_login(request):

    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Your username or password is incorrect')

    
    context={}
    return render(request,'NimapApp/login.html',context)

def home_p(request):
    return render(request,'NimapApp/home.html')