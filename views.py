from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from EkartDogApp.models import Product
from django.db.models import Q 
def register(request):
    context={}
    if request.method=="POST":
        uname=request.POST["uname"]
        upass=request.POST["upass"]
        ucpass=request.POST["ucpass"]
        if uname=="" or upass=="" or ucpass=="":
            context["errmsg"]="Fields cannot be Empty"
            return render (request,"register.html",context)
        elif upass!=ucpass:
            context["errmsg"]="password and confirm password didnt match"
            return render (request,"register.html",context)
        else:
            try:
                u=User.objects.create(username=uname,email=uname)
                u.set_password(upass)
                u.save()
                context["success"]="User Created SuccessFully"
                return render (request,"register.html",context)
                """return HttpResponse("User Created SuccessFully")"""
            except Exception:
                context["errmsg"]="user with same username already exist "
                return render (request,"register.html",context)
    else:
        return render (request,"register.html",context)
  
def loginuser(request):
       context={}
       if request.method=='POST':
           uname=request.POST.get('uname')
           upass=request.POST.get('upass')
           if uname=="" or upass=="":
               context["errmsg"]="Fields cannot be empty"
               return render(request,"login.html",context)
           else:
               user=authenticate(request , username=uname , password=upass)
               if user is not None:
                   login(request,user)
                   return redirect("/index")
               else:
                   context["errmsg"]="Credientials are incorrect"
                   return render(request,"login.html",context)
       else:
           return render(request,"login.html",context)      

def logout(request):
    logout(request)
    #return redirect("home/")
    return redirect('login') 
def catfilter(request,cv):#cv-catrgory value
    q1=Q(is_active=True)#Q- it is used for defining the conditions 
    q2=Q(cat=cv)
    p=Product.objects.filter(q1 & q2)#q1 and q1 are conditions.
    print(p)
    context={}
    context['Products']=p
    return render(request,'index.html',context)
def home(request):
    context={}
    p=Product.objects.filter(is_active=True)#This line will print all the products which are in active state
    context['Products']=p # Here products means the table which is in Admin side
    # print(p)
    return render(request,'index.html',context) 
def sort(request,sv):#sv=sorting value
    print(type(sv))#This will print the type of product whether it is int,str,etc
    if sv==0:
        col="pcost"#ascending
    else:
        col="-pcost"#descending
    p=Product.objects.filter(is_active=True).order_by(col)# This line will filter all the products which are in the active state 
    context={}
    context["Products"]=p
    return render(request,"index.html",context)

def range(request):
    min=request.GET['min']
    max=request.GET['max']
    q1=Q(pcost__gte=min)
    q2=Q(pcost__lte=max)
    q3=Q(is_active=True)
    p=Product.objects.filter(q1 & q2 & q3)
    context={}
    context["Products"]=p
    print(min)
    print(max)
    return render(request,'index.html',context)
def navbar(request):
    return render(request,"navbar.html")
def footer(request):
    return render(request,'footer.html')
def about(request):
    return render(request,'aboutus.html')
def contact(request):
    return render(request,'contact.html')
def indexpage(request):
    return render(request,"index.html")
def cart(request):
    return render(request,"cart.html")
def placeorder(request):
    return render(request,"place_order.html")
def product(request):
    return render(request,"product.html")