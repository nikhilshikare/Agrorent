from unittest.util import _MAX_LENGTH
import django
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.forms import CharField
from django.dispatch import receiver
from django.db.models.signals import post_save

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


        
#<------Model Named addUser to Extend the inbuild Django UserModel Starts here -------->