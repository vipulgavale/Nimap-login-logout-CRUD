from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProjectInfo(models.Model):
    project = models.CharField(null=True,max_length=100)

class MyNimapInfo(models.Model):
    client = models.ManyToManyField(ProjectInfo)
    date = models.DateField()

class Clientinfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    


