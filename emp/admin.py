from django.contrib import admin
from .models import Emp

# Register your models here.

#models will get register from the site of admin

class EmpAdmin(admin.ModelAdmin):
    #used for displaying
    list_display=('name','working','emp_id','phone')
    #this function is used to edit the functions (here working and employee id)
    list_editable=('working','emp_id')
    search_fields=('name','emp_id')

admin.site.register(Emp,EmpAdmin)
