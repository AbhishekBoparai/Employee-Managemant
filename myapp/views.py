from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    #code for reteriving data from templates to views.py
    if request.method=='POST':
        check=request.POST['check']
        print(check)





    isActive=True
    name="Learn to Code"
    list_of_programs=[
        'WAP to check evn or odd',
        'WAP to check prime numbers',
        'WAP to print all the prime numbers',
        'WAP to print pascals triangle'
    ]

    student={
        'student_name':'Rahul',
        'student_collage':"YZX",
        'student_city':'LUKHNOW'

    }
    
    data={
        #key:value
        'student':student,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        
    }
    #print("test function is called from view")
    #return HttpResponse ("<h1> Hello World </h1>")
    #return render(request,template_name,{dictionary if there is any dynamic data is present})

    #reffereing data to home.html
    return render(request,"home.html",data)


def about(request):
    #return HttpResponse("<h1> This is about page </h1>")
    return render(request,"about.html",{})

def services(request):
    #return HttpResponse("<h1> This is service page </h1>")
    return render(request,"services.html",{})