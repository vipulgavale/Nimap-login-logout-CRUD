from NimapApp.models import MyNimapInfo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from NimapApp.forms import ClientInfoForm,ClientUserInfoForm
from django.contrib import messages
from django.views import View
# Create your views here.

def client_registration(request):
    form = ClientUserInfoForm()

    if request.method == 'POST':
        form=ClientUserInfoForm(request.POST)

        if form .is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"Account Created for "+ user +" successfully")
            return redirect('login')

    context= {'form':form}
    return render(request,'NimapApp/registration.html',context)

def client_login(request):

    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect!')
    context={}
    return render(request,'NimapApp/login.html',context)

def client_logout(request):
    logout(request)
    return redirect('login')

class Home(View):
    def get(self,request):
        stu_data=MyNimapInfo.objects.all()
        return render(request,'NimapApp/home.html',{'studata':stu_data})

class Add_Employee(View):
    def get(self,request):
        fm=ClientInfoForm()
        return render(request,'NimapApp/add-info.html',{'form':fm})
    
    def post(self,request):
        fm=ClientInfoForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')
        else:
            return render(request,'NimapApp/add-info.html',{'form':fm})
        
class Delete_Employee(View):
    def post(self,request):
        data=request.POST
        id = data.get('id')
        empldata = ClientInfoForm.objects.get(id=id)
        empldata.delete()
        return redirect('home')

class EditEmployee(View):
    def get(self,request,id):
        emp=MyNimapInfo.objects.get(id=id)
        fm=ClientInfoForm(instance=emp)
        return render(request,'NimapApp/edit-info.html',{'form':fm})

    def post(self,request,id):
        emp=MyNimapInfo.objects.get(id=id)
        fm=ClientInfoForm(request.POST, instance=emp)
        if fm.is_valid():
            fm.save()
            return redirect('home')
