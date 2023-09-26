from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp

# Create your views here.
def emp_home(request):
    # whatever information I have entered in the form we have to show that on home page
    #sending data to views to template
    emps=Emp.objects.all()
    

    return render(request,"emp/home.html",{
        'emps':emps
    })

def add_emp(request):
    if request.method=="POST":
        #fetch data (Jo data new employee ne add kiya hai use fetch karenge)
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_Department=request.POST.get("emp_department")

        #create model object and set the data
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        if emp_working is None:
            e.working=False
        else:
            e.working=True

        e.Department=emp_Department

        #save the object
        e.save()

        



        #after clicking on add employee it will open url /emp/home/ 
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")



def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })
    