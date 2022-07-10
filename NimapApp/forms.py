from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from NimapApp.models import ProjectInfo,MyNimapInfo,Clientinfo

class ProjectInfoForm(forms.ModelForm):
    
    class Meta:
        model = ProjectInfo
        fields = ('project',)

class ClientInfoForm(forms.ModelForm):
    
    class Meta:
        model = MyNimapInfo
        fields = ("client","date",)

class ClientUserInfoForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1","password2")


