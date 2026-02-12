from django.contrib import admin
from student.models import Profile
# Register your models here.

# admin.site.register(Profile)
#  this only shows the single detail in admin


# for complete rows and cols in admin panel we use this
class Profileadmin(admin.ModelAdmin):
    list_display = ('name','roll','email','city')
    
# it takes the actual table form the profile and then the profileadmin that telll what to 
# show into the aadmin panel
admin.site.register(Profile,Profileadmin)