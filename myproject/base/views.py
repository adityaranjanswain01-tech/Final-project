from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q


# Create your views here.

@login_required(login_url="login_")
def home(request):
    no_match=False
    trending=False
    offer=False
    if "search" in request.GET:
        search = request.GET['search']
        data  = Product.objects.filter(Q(pname__icontains=search) | Q(pdesc__icontains=search))
        if len(data)==0:
            no_match=True
    elif 'category' in request.GET:
        category=request.GET['category']
        data = Product.objects.filter(pcategory=category)
    elif 'trending' in request.GET:
        data= Product.objects.filter(trending=True)
        trending=True
    elif 'offer' in request.GET:
        data= Product.objects.filter(offer=True) 
        offer=True
    else:
        data=Product.objects.all()
        
    a=Product.objects.all()
    category=[]
    for i in a:
        if i.pcategory not in category:
            category+=[i.pcategory]
    
    return render (request,"home.html",{"data":data,"no_match":no_match,"search_bar":True,"trending":trending,"offer":offer,'category':category})


@login_required(login_url='login_')
def cart(request):
    data_count=Cartmodel.objects.filter(host=request.user).count()
    totalprice=0
    cnt=0
    data=Cartmodel.objects.filter(host=request.user)
    for i in data:
        totalprice+=i.totalprice
        cnt+=1
    return render(request,'cart.html',{"data":data,"totalprice":totalprice})

@login_required(login_url='login_')
def add_cart(request,id):
    product=Product.objects.get(id=id)
    try:
        cp = Cartmodel.objects.get(pname = product.pname,host=request.user)
        cp.quantity +=1
        cp.totalprice +=product.price
        cp.save()
    except:    
        Cartmodel.objects.create(
            pname=product.pname,
            price=product.price,
            pcategory=product.pcategory,
            quantity=1,
            totalprice = product.price,
            host = request.user,    
        )
    return redirect('cart')

def remove(request,id):
    cartproduct=Cartmodel.objects.get(id=id)
    cartproduct.delete()
    return redirect ("cart")

def increment(request,id):
    cartproduct=Cartmodel.objects.get(id=id)
    cartproduct.quantity+=1
    cartproduct.totalprice+=cartproduct.price
    cartproduct.save()
    return redirect ('cart')

def decrement(request,id):
    cartproduct=Cartmodel.objects.get(id=id)
    if cartproduct.quantity>1:
        cartproduct.quantity-=1
        cartproduct.totalprice-=cartproduct.price
        cartproduct.save()
    else:
        cartproduct.delete()
    return redirect ('cart')

def support(request):
    return render(request,'support.html')
def know_us(request):
    return render(request,'know_us.html')