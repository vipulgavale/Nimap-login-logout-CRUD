from django.urls import path
from NimapApp import views


urlpatterns = [
    path('',views.client_registration,name='registration'),
    path('login/',views.client_login,name='login'),
    path('home/',views.client_login,name='home')
]
