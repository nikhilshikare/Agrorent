from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import render , redirect
from django.http import HttpResponse
from agrorentapp.models import  addUser 
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

# <------------------Global Method Send Email Function Start here ------------------------------>
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

# <------------------Add/show Agro-Tools class  start from here------------------------------>

class Tools:
         # <------------------Add Tool function is start here------------------------------>
    def add_tool(request):
        if request.user.is_authenticated:
            return render(request,"add_tool.html")
        else:
            return redirect("/sign_in")
         # <------------------View Tool function is start here------------------------------>
    def view_tools(request):
        return HttpResponse("hii view tools")
         # <------------------Update toolis start here------------------------------>
    def update_tool(request):
        return HttpResponse("hii update tools")


# <------------------Autintication sign in sign up class start here------------------------------>
class Auth:

    #< **********Common function to check redundancy of username , email or phone in database********>
    def check_redundent_info(username,phone,email):
            # Now Perform some validation If Username , Number or email exists in database
            if User.objects.filter(username=username).exists():
                #send 0 to show Username exist in db
                return 0
            elif addUser.objects.filter(phone=phone).exists():
                #send 1 to show Phone exist in db
                return 1
            elif User.objects.filter(email=email).exists():
                #send 2 to show email exist in db
                return 2                
            else:
                #ereturn 3 to say all ok
                return 3

    #< **********End of Common function to check redundancy of username , email or phone in database********>
         # <------------------Send otp is start here------------------------------>
    def send_otp(request):
        if request.method =='POST':
            email = request.POST.get('email')
            fname = request.POST.get('fname')
            username = request.POST.get('username')
            phone = request.POST.get('phone')
            # call function to check Redundancy of email , phone, username
            flag =Auth.check_redundent_info(username,phone,email)
            if flag==3:
                otp = random.randrange(1000,10000)
                #call send msg function
                flag = send_email("Your otp For Signup",f"Hii {fname},greeting from Agrorent Your Otp For Verfication Is --> {str(otp)}",email)
                if flag: #send otp if all work fine
                    return HttpResponse(otp)
                else:   #send -1 as error flag
                    return HttpResponse("-1")
            else:
                return HttpResponse(str(flag))

      # <---------------------------Signin  Function is start here------------------------------>

    def sign_in(request):
        if request.method =="POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate( request,username=username, password=password)
            # check if user entered correct crediantials
            if user is not None:
                login(request, user)
                #send Signal 1 to indicate login succesfully
                return HttpResponse("1")
                # return redirect("/")
                # A backend authenticated the credentials
            else:
                # No backend authenticated the credentials
                #send Signal 0 to indicate Something went Wrong
                return HttpResponse("0")
        else:
            return render(request,"sign_in.html")

    

        # <------------------Signup function is start here------------------------------>

    def sign_up(request):
        # cHECK FOR pOST method and get the All required field
        if request.method =='POST':
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            password = request.POST.get('password')
            username = request.POST.get('username')
            # call function to check Redundancy of email , phone, username
            flag = Auth.check_redundent_info(username,phone,email)
            if flag==3:
                user = User.objects.create_user(username=username, password=password, email=email,first_name=fname,last_name=lname)
                addUser(user=user,phone=phone).save()
                #send 3 to Indicate All Above Mentioned Field Are Unique And saved succesully.
                return HttpResponse(3)
            else:
                return HttpResponse(str(flag))

        return render(request,"sign_up.html")

    # <------------------Logout/Sign-out  function is start here------------------------------>

    def sign_out(request):
        logout(request)
        return redirect("/")
        



