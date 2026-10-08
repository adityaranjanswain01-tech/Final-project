from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_(request):
    if request.method=='POST':
        u=authenticate(username=request.POST['username'],password=request.POST['password'])
        if u:
          login(request,u)
          return redirect('home')
        else:
              return render(request,'login_.html',{"error":"invalid user name or password"})
    return render(request,"login_.html")

def register(request):
    if request.method=="POST":
        try:
            u = User.objects.get(username=request.POST['username'])
            return render(request,'register.html',{"error":"USER ALREADY EXISTs"})
        except:
            u= User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            username = request.POST['username'],
        )
        u.set_password(request.POST['password'])
        u.save() 
    return render(request,"register.html")

@login_required(login_url="login_")
def profile(request):
    return render(request,"profile.html")

def forgot(request):
    if request.method == 'POST':
        username = request.POST['username']
        try:
            u = User.objects.get(username=username)
            print(u)
            request.session['fp_user'] = u.username
            return redirect('new_password')
        except:
            return render(request,'forgot.html',{'error':'Invalid Username'})
    return render(request,'forgot.html')

def new_password(request):
    username = request.session.get('fp_user')
    print(username)
    if username is None:
        return redirect('forget_pass')
    user = User.objects.get(username=username)
    if request.method == 'POST':
        new_pass = request.POST['new']
        if user.check_password(new_pass):
            return render(request,'new.html',{'error':'New Password should not be same as old password'})
        user.set_password(new_pass)
        user.save()
        del request.session['fp_user']
        return redirect('login_')
    return render(request,'newpass.html')

def update(request):
    data=request.user
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        data.first_name = fname
        data.last_name = lname
        data.email = email
        data.save()
        return redirect('profile')
    return render(request,'update.html')


@login_required(login_url='login_')
def reset(request):
    if request.method == 'POST':
        if 'old_pass' in request.POST:
            u = authenticate(username=request.user.username,password=request.POST['old_pass'])
            print(u)
            if u:
                return render(request,'reset.html',{'new':True})
            else:
                return render(request,'reset.html',{'error':'Incorrect Old Password'})
        if 'new_pass' in request.POST:
            new = request.POST['new_pass']
            if request.user.check_password(new):
                return render(request,'reset.html',{'error':'New password should not be same as old password','new':True})
            request.user.set_password(new)
            request.user.save()
            return redirect('logout_')
    return render(request,'reset.html')

@login_required(login_url="login_")
def logout_(request):
    logout(request)
    return redirect('login_')

