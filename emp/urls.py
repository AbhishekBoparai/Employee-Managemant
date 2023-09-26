from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
     path("home/",emp_home),
     path("add-emp/",add_emp),
     #URL for deleting an employee from the data present
     path("delete-emp/<int:emp_id>",delete_emp),
     path("update-emp/<int:emp_id>",update_emp),
]