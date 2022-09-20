from django.contrib import admin
from django.urls import path,include
from agrorentapp import views

urlpatterns = [
    path('',views.home,name='home'),
    #<--------- Authentication releted path / urls start here ------->

    path('sign_up',views.Auth.sign_up,name='sign_up'),
    path('sign_in',views.Auth.sign_in,name='sign_in'),
    path('sign_out',views.Auth.sign_out,name='sign_out'),
    path('otp',views.Auth.send_otp,name='otp'),

    #<--------- Authentication releted path / urls ends here ------->

    #<--------- Class Tools releted path / urls start here ------->

    path('add_tools',views.Tools.add_tool,name='add_tools'),
    path('view_tools',views.Tools.view_tools,name='view_tools'),
    path('update_tool',views.Tools.update_tool,name='update_tool'),

    #<--------- Class Tools releted path / urls ends here ------->
]
