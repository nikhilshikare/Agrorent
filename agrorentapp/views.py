from json import tool
from tkinter.tix import Tree
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from agrorentapp.models import addUser,Booking,Request , Tool
from django.core.mail import send_mail
from agrorentapp.forms import ToolForm
import random 
import datetime
from django.core.files.storage import default_storage


# username and Password for django super user
# Username:-nikhil & Password:-nikhil9869
# (Please creatE SuperUser Then Store It here If you Have HABIT Of Forgeting passwords)
#Email And Password:
#Email :- agrorent2022@gmail.com && Password:-agrorent9869@#
# Create your views here.

def home(request):
    return render(request,"home.html")

def upload_adhar(request):
    if request.method =='POST':
        adhar = request.POST.get('adhar')
        if addUser.objects.filter(adhar=adhar).exists():
            return HttpResponse("0")#same Adhar No Exist return 0
        else:
           
            addUser.objects.filter(user=request.user).update(adhar=adhar)
            return HttpResponse("1")#Return 1 For all
    else:
        return HttpResponse("-1")#for Unknown error

# <------------------Global Method Send Email && 6 digit random Generate Function Start here ------------------------------>
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

def random_6_digit():
    return random.randrange(100000,1000000)
    
    #<------Global Method For Checking if AgroTool is Actively Booked Or Not------------->

def tool_still_booked(tool_id):
    try:
        if Booking.objects.filter(tool_id=tool_id).filter(is_booked=1).exists():
            return 1 # send "1" to indicate tool booked 
        else:
            return 0 # send "0" to indicate tool not booked 
    except:
        return -1 # send "-1" to indicate some error occure while firing query.. 




# <------------------Add/show Agro-Tools class  start from here------------------------------>



class Request_Tool:

      # <------------------Make Request For Agro-Tool function is start here------------------------------>
    def book_tool(request):
          #<----Internel function To Check Redundency of request ID In database START-->
        def genrate_booking_id(tool_id):
            booking_id = str(random.randrange(1000,10000))+str(tool_id)
            if Booking.objects.filter(booking_id=booking_id).exists():
                genrate_booking_id()
            else:
                return booking_id
        #<----Internel function To Check Redundency of request ID In database END-->

        if request.user.is_authenticated:
             if request.method =='POST':
                tool_id = request.POST.get("tool_id")
                tool_owner = request.POST.get("tool_owner")
                request_id = request.POST.get("request_id")
                date_data =   Request.objects.filter(request_id=request_id).values('required_from','required_till')
                required_from=date_data[0]['required_from']
                required_till=date_data[0]['required_till']
                if(tool_still_booked(tool_id)==1):
                    return HttpResponse("0")#indicate tool may booked or some technical error
                else:
                    conform_book_tool = Booking.objects.create(booking_id=genrate_booking_id(tool_id),booking_amt_paid="1000",rented_to=request.user.username,
                    owner_name=tool_owner,tool_id=tool_id,is_booked=True,required_from=required_from,
                    required_till=required_till)
                    conform_book_tool.save()
                    Request.objects.filter(tool_id=tool_id).delete()
                    return HttpResponse("1")#to indicate Request made..
        else:
            return redirect("/sign_in")

      # <------------------Make Request For Agro-Tool function is start here------------------------------>


         # <------------------Make Request For Agro-Tool function is start here------------------------------>
    def request_tool(request):

          #<----Internel function To Check Redundency of request ID In database START-->
        def genrate_request_id():
            request_id = str(random.randrange(1000,10000))+request.user.adduser.phone+str(random_6_digit())
            if Request.objects.filter(tool_id=tool_id).exists():
                genrate_request_id()
            else:
                return request_id
        #<----Internel function To Check Redundency of request ID In database END-->

        if request.user.is_authenticated:
             if request.method =='POST':
                tool_id = request.POST.get("tool_id")
                tool_owner = request.POST.get("tool_owner")
                required_from = request.POST.get("required_from")
                required_till = request.POST.get("required_till")
                if(tool_still_booked(tool_id)==1):
                    return HttpResponse("0")#indicate tool may booked or some technical error
                else:
                    request_tool = Request.objects.create(request_id=genrate_request_id(), send_to=tool_owner,tool_id=tool_id,send_from=request.user.username,
                    is_accepted=0,is_rejected=0,required_from=required_from,required_till=required_till)
                    request_tool.save()
                    return HttpResponse("1")#to indicate Request made..
        else:
            return redirect("/sign_in")

      # <------------------Make Request For Agro-Tool function is start here------------------------------>


    def requests(request):
        if request.user.is_authenticated:
            status=request.GET.get("status")
   # <------------------Request send By Others--->
            send_to_lst=[]
            sender_data=[]
            request_to=Request.objects.filter(send_to=request.user.username).values()
            for i in request_to:
                send_to_lst.append(i)
            try:
                for i in User.objects.filter(username=request_to[0]['send_from']).values('first_name','last_name'):
                    sender_data.append(i)
            except:
                sender_data.append("No Request")
           
  # <------------------Request send By Me ---->
            send_from_lst=[]
            request_from=Request.objects.filter(send_from=request.user.username).values()
            for i in request_from:
                send_from_lst.append(i)
            return render(request,"requests.html",context={'status':status,'send_to_lst':send_to_lst,'send_from_lst':send_from_lst,'sender_data':sender_data})
        else:
            return redirect("/sign_in")

# <------------------Add/show Agro-Tools class  start from here------------------------------>

    def requests_action(request):
        if request.user.is_authenticated:
            btn_action = request.GET.get("btn_action")
            request_id = request.GET.get("request_id")
            if btn_action == "0":
                Request.objects.filter(request_id=request_id).update(is_rejected=True)
                return redirect("/requests?status=0")
            elif btn_action == "1":
                Request.objects.filter(request_id=request_id).update(is_accepted=True)
                return redirect("/requests?status=1")
            else:
           
                return redirect("/requests?status=2")
               
   

    # <------------------Add/show Agro-Tools class  start from here------------------------------>




class Tools:

        # <------------------View Uploaded  Tool function is start here------------------------------>
    def search_tool(request):
        if request.user.is_authenticated:
            if request.method =='POST':
                location = request.POST.get('location')
                tool_type = request.POST.get('tool_type')
                tools_data_lst=[]
                tools_data= Tool.objects.all()
                for i in tools_data:
                    tools_data_lst.append(i)
                context={
                        "tools_data_lst":tools_data_lst,
                        }   
                return render(request,"search.html",context=context)
            else:
                return render(request,"search.html")
        else:
            return redirect("/sign_in")
         # <------------------Add Tool function is start here------------------------------>
    def add_tools(request):
        #<----Internel function To Check Redundency of Tool ID In database START-->
        def genrate_tool_id():
            tool_id = request.user.adduser.phone+str(random_6_digit())
            if Tool.objects.filter(tool_id=tool_id).exists():
                genrate_tool_id()
            else:
                return tool_id
        #<----Internel function To Check Redundency of Tool ID In database END-->
        if request.user.is_authenticated:
            #random_6_digit()
            form = ToolForm()
            if  request.method =='POST':
                form = ToolForm(request.POST,request.FILES)
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.tool_id = genrate_tool_id()
                    obj.username = request.user.username
                    obj.save()

                    context={
                    'form':form,
                    'status':"1",
                    }
                   
                    return render(request,"add_tool.html",context) #return context= 1 To indicate all OK
                else:
                    context={
                        'form':form,
                        'status':"0",
                    }
                    return render(request,"add_tool.html",context)#return context =0 To indicate Something is Wrong
            else:
                context={
                        'form':form,
                        'status':"-1",
                    }
                return render(request,"add_tool.html",context)
        else:
            return redirect("/sign_in")

         # <------------------View Uploaded  Tool function is start here------------------------------>
    def my_tools(request):
        if request.user.is_authenticated:
            tools_data_lst=[]
            # tools_data = Tool.objects.values('tool_spec_1', 'tool_spec_2','tool_type','rent_price','tool_photo').filter(username=request.user)
            tools_data= Tool.objects.all().filter(username=request.user)
            for i in tools_data:
                tools_data_lst.append(i)
            context={
                    "tools_data_lst":tools_data_lst,
                    }   
            return render(request,"my_tools.html",context=context)
        else:
            return redirect("/sign_in")

        # <------------------Update tools strt here------------------------------>
    def update_tool(request):
        return HttpResponse("hii update tools")

        # <------------------Update tools strt here------------------------------>
    def show_info(request):
        if request.user.is_authenticated:
            tool_id = request.GET.get("tool_id")
            action_btn_status = request.GET.get("action_btn_status")
            tool_booked_status=2
            if(tool_still_booked(tool_id)==1):
                tool_booked_status = 1
            if(tool_still_booked(tool_id==-1)):
                tool_booked_status= -1
            if (tool_still_booked(tool_id)==0):
                tool_booked_status = 0
            #<------------------------->
            request_send_status=0
            request_data=''
            try:
                if Request.objects.filter(tool_id=tool_id).filter(send_from=request.user.username).exists():
                    request_send_status = 1# send "1" to indicate Request sended
                    request_data= Request.objects.filter(tool_id=tool_id).filter(send_from=request.user.username).values('required_till','required_from','is_accepted','is_rejected','request_id')
                else:
                    request_send_status = 0# send "0" to indicate Not Request sended
            except:
                request_send_status = -1 # send "-1" to indicate some error occure while firing query.. 

            #<------------------------->
            tools_data_lst=[]
            tools_data= Tool.objects.all().filter(tool_id=tool_id)
            for i in tools_data:
                tools_data_lst.append(i)
            context={
                    "tools_data_lst":tools_data_lst,
                    "tool_booked_status":tool_booked_status,
                    "request_send_status":request_send_status,
                    "request_data":request_data,
                    "action_btn_status":action_btn_status,
                    }   
            return render(request,"show_full_info.html",context=context)
        else:
            return redirect("/sign_in")
            
        # <------------------Delete tools strt here------------------------------>
    def delete_tool(request):
        if request.user.is_authenticated:
            tool_id = request.POST.get('tool_id')
            try:
                tool_url_path = Tool.objects.filter(tool_id=tool_id).values('tool_photo')
                for i in tool_url_path:
                    tool_path=i['tool_photo']
                default_storage.delete(tool_path) #first delete photo from Media folder
                Tool.objects.filter(tool_id=tool_id).delete() # then delete data from database.
                Request.objects.filter(tool_id=tool_id).delete() # then delete All the Request Related With Tool database.
                return HttpResponse("1")
            except:
                return HttpResponse("0")
        return HttpResponse("0")
        

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
        



