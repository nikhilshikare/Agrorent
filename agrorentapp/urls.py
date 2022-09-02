from django.contrib import admin
from django.urls import path,include
from agrorentapp import views

urlpatterns = [
    path('',views.home,name='home'),
        path('sign_up',views.Auth.sign_up,name='sign_up'),
    path('sign_in',views.Auth.sign_in,name='sign_in'),
    path('sign_out',views.Auth.sign_out,name='sign_out'),
    path('otp',views.Auth.send_otp,name='otp'),
]
