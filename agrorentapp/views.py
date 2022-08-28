from sys import flags
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
import random


# username and Password for django super user
# Username:-nikhil & Password:-nikhil9869
# (Please creatE SuperUser Then Store It here If you Have HABIT Of Forgeting passwords)
#Email And Password:
#Email :- agrorent2022@gmail.com && Password:-agrorent9869@#


# Create your views here.

def home(request):
    return render(request,"home.html")

# <------------------Send Email Function Start here ------------------------------>
def send_email(sub,message,reciver_email):
    try:
        send_mail(
        ''+sub+'',
        ''+message+'',
        'agrorent2022@gmail.com',
        [reciver_email],
        fail_silently=False,
        )
        return 1
    except:
        return 0

# <------------------Autintication sign in sign up class start here------------------------------>
class Auth:
    def send_otp(request):
        if request.method =='POST':
            email = request.POST.get('email')
            fname = request.POST.get('fname')
            otp = random.randrange(1000,10000)
            #call send msg function
            flag = send_email("Your otp For Signup",f"Hii {fname},greeting from Agrorent Your Otp For Verfication Is --> {str(otp)}",email)
            if flag: #send otp if all work fine
                return HttpResponse(otp)
            else:   #send o as error flag
                return HttpResponse("0")
        else:
            return HttpResponse("0")

    def sign_in(request):
        return render(request,"sign_in.html")

    def sign_up(request):
        if request.method =='POST':
            pass
        return render(request,"sign_up.html")

    def sign_out(request):
        return HttpResponse("Sign Out please")



