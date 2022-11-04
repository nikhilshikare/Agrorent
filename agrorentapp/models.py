from django.db import models
from django.contrib.auth.models import User
import datetime
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

# Create your models here.


#<------Model Named addUser to Extend the inbuild Django UserModel Starts here -------->
class addUser(models.Model):
    #<-------------For Extending user field In Order to add Phone as Additional Field-------->
    # <-----Accesing data For Selected Profile ---------->
    # <---------users = User.objects.all().select_related('addUser')---------------> 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(null=False,blank=False,unique=True,max_length=12)
    adhar = models.CharField(null=True,max_length=12)

    def __str__(self):
        return self.user.username


#<----------Model Named addUser to Extend the inbuild Django UserModel Ends here ------------>

#<----------Model Named Tools to add tool Starts Here here ------------>

#<***********image Renaming According to Id  Starts Here here ************>

@deconstructible
class PathRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.tool_id, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

path_and_rename = PathRename("images")

#<***********image Renaming According to Id  Ends Here here ************>

class Tool(models.Model):
    tool_id     = models.CharField(unique=True ,primary_key=True, null=False ,max_length=20)#'Phone + 6 digit random no'
    username    = models.CharField(unique=False ,max_length=50,blank=False)#ownerusername
    tool_spec_1 = models.CharField(max_length=200,blank=True)
    tool_spec_2 = models.CharField(max_length=200,blank=True)
    tool_info   = models.TextField(blank=True) 
    rent_price  = models.CharField(max_length=9)
    tool_type = models.CharField(max_length=200,blank=True)
    location = models.CharField(max_length=200,blank=True)
    tool_photo = models.ImageField(upload_to=path_and_rename)

    def __str__(self):
        return self.tool_type

        
#<----------Model Named Tools to add tool Ends Here here ------------>
#<----------Model Named Request to send And recive request Starts Here here ------------>

class Request(models.Model):
    request_id   = models.CharField(unique=True ,primary_key=True, null=False ,max_length=20)#'4 digit+Phone + 6 digit random no'
    send_to     = models.CharField(unique=False ,max_length=50,blank=False)#recever username
    send_from  = models.CharField(unique=False ,max_length=50,blank=False)#sender username
    #Current_dateTime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    request_time = models.DateTimeField( default=datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S") , blank=True)
    tool_id   = models.CharField(null=False ,max_length=20)
    is_accepted  = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    required_from =  models.DateTimeField(blank=True)
    required_till = models.DateTimeField(blank=True)
    def __str__(self):
        return self.request_id

#<----------Model Named Request to send And recive request Ends Here here ------------>
#<----------Model Booking Table to store all bookng info Starts Here here ------------>

class Booking(models.Model):
    booking_id   = models.CharField(unique=True ,primary_key=True, null=False ,max_length=20)#tool_id+4 digit no
    booking_amt_paid = models.CharField(max_length=12)
    rented_to     = models.CharField(unique=False ,max_length=50,blank=False)#booking_doneby_person username
    owner_name  = models.CharField(unique=False ,max_length=50,blank=False)#tool_owner_name username
    booking_time = models.DateTimeField( default=datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"), blank=True)
    tool_id   = models.CharField(null=False ,max_length=20)
    is_booked  = models.BooleanField(default=False)
    required_from =  models.CharField(max_length=12,blank=True)
    required_till = models.CharField(max_length=12,blank=True)
    def __str__(self):
        return self.booking_id



#<----------Model Booking Table to store all bookng info Ends Here here ------------>