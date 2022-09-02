from django.contrib import admin
from agrorentapp.models import addUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

#<--------- Making of Inline class For adduser To save Phone No--->
class addUserInline(admin.StackedInline):
    model = addUser
    can_delete =  False
    verbose_name_plural = 'addUsers'

#<--------- Customized the Admin class For In order to save and edit info--->   
class CustomizedUserAdmin(UserAdmin):
    def add_view(self,*args,**kwargs,):
        self.inlines=[]
        return super(CustomizedUserAdmin,self).add_view(*args,**kwargs)
    
    def change_view(self,*args,**kwargs,):
        self.inlines=[addUserInline]
        return super(CustomizedUserAdmin,self).change_view(*args,**kwargs)

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)


#<---- Customization for addUser Model (achived by OneToOne Field is Complete Here)----->

# Register your models here.

admin.site.register(addUser)