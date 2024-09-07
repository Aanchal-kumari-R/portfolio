from django.shortcuts import render  
from .models import Contact 


# Create your views here. 

def home(request): 
    return render(request,"home.html")

def about(request): 
    return render(request,"about.html")

def projects(request):  
    projects_show = [ 
        { 
            "title":"Crud Operation", 
            "path": "images/Crud.PNG"
        }, 

        { 
            "title":"Ecommerce Website", 
            "path":"images/ecom_website.PNG" 
        },  

        {  
           "title":"Portfolio", 
           "path":"images/portfolio.PNG"
        }, 

        { 
            "title":"API Based Ecommerce", 
            "path":"images/ecomsite.PNG"
        }  
        

    ]
    return render(request,"projects.html",{"projects_show":projects_show}) 

def experience(request):  
     experience = [ 
         { 
            "Company" : "ABC", 
            "Position": "Python Developer"
         }, 

         { 
            "Company":"ABC2", 
            "Position":"Python Developer"
         }, 

         { 
            "Company":"ABC3", 
             "Position":"Python Developer"
         }
     ]

     return render(request,"experience.html",{"experience":experience}) 

def certificate(request): 
    return render(request,"certificate.html")

def contact(request):   
    if request.method == "POST":  
        name = request.POST.get('name','') 
        password = request.POST.get('password','')   
        phone = request.POST.get('phone','')
        text = request.POST.get('text','') 
        contact = Contact(name=name,password=password,phone=phone,text=text) 
        contact.save() 
        


    return render(request,"contact.html")


def resume(request): 
    return render(request,"resume.html")