from django.shortcuts import render 


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
  

    return render(request,"experience.html")

