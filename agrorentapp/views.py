from django.shortcuts import render
from django.http import HttpResponse


# username and Password for django super user
# Username:-nikhil & Password:-nikhil9869
# (Please creatE SuperUser Then Store It here If you Have HABIT Of Forgeting passwords)



# Create your views here.

def home(request):
    return render(request,"home.html")