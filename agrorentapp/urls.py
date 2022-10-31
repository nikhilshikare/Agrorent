from django.contrib import admin
from django.urls import path,include
from agrorentapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    #<--------- Authentication releted path / urls start here ------->

    path('sign_up',views.Auth.sign_up,name='sign_up'),
    path('sign_in',views.Auth.sign_in,name='sign_in'),
    path('sign_out',views.Auth.sign_out,name='sign_out'),
    path('otp',views.Auth.send_otp,name='otp'),

    #<--------- Authentication releted path / urls ends here ------->

    #<--------- Adhar Upload releted path / urls start here ------->

    path('upload_adhar',views.upload_adhar,name='upload_adhar'),

    #<--------- Adhar Upload releted path / urls Ends here ------->
    #<--------- Class Tools releted path / urls start here ------->
    path('add_tools',views.Tools.add_tools,name='add_tools'),
    path('my_tools',views.Tools.my_tools,name='my_tools'),
    path('show_info',views.Tools.show_info,name='show_info'),
    path('update_tool',views.Tools.update_tool,name='update_tool'),
    path('delete_tool',views.Tools.delete_tool,name='delete_tool'),
    path('search_tool',views.Tools.search_tool,name='search_tool'),
    #<--------- Class Tools releted path / urls ends here ------->
    #<--------- Class Request releted path / urls start here ------->
    path('requests_action',views.Request_Tool.requests_action,name='requests_action'),
    path('requests',views.Request_Tool.requests,name='requests'),
    path('request_tool',views.Request_Tool.request_tool,name='request_tool'),
    path('book_tool',views.Request_Tool.book_tool,name='book_tool'),
    #<--------- Class Request releted path / urls ends here ------->
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#To store The Images and Media Files
