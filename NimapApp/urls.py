from django.urls import path
from NimapApp import views
from NimapApp.views import Home,Add_Employee,Delete_Employee,EditEmployee


urlpatterns = [
    path('',views.client_registration,name='registration'),
    path('login/',views.client_login,name='login'),
    path('logout/',views.client_logout,name='logout'),
    path('home/',Home.as_view(),name='home'),
    path('add/',Add_Employee.as_view(),name='add-employee'),
    path('delete/',Delete_Employee.as_view(),name='delete-employee'),
    path('edit/<int:id>/',EditEmployee.as_view(),name='edit-employee')

    
    
]
