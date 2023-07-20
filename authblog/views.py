
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404, render, redirect
from .models import Profile

# Create your views here.

def handleRegister(request):
    if request.method=="POST":
        email= request.POST['email']
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        username=request.POST['username']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            print('password is not matching')
            return render(request,'register.html')                   
        try:
            if User.objects.get(username=username):
                print('user already has an account with us')
                return render(request,'register.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(username,email=email, password= password, first_name= firstname, last_name= lastname)
        
        user.save()
        print('user saved')
        user.is_active=True
        print('user activated')
        return redirect('/authentication/login/')
    return render(request,"register.html")

def handleLogin(request):
    if request.method=="POST":
        username=request.POST['username']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            print('user logged in')         
            return redirect('/')

        else:
            print('invalid credential')
            return redirect('/authentication/login')

    return render(request,'login.html')  

def handleLogout(request):
    logout(request)
    print('logged out')
    return redirect('/authentication/login')

def viewProfile(request, user_id):
    user= get_object_or_404(User, pk= user_id)
    
    return render(request, 'view_profile.html', {'user': user})


# write logic for editing profile

def editProfile(request, user_id):
    user= get_object_or_404(User, pk= user_id)
    profile= user.profile
    if request.method=='POST':
        phonenumber= request.POST['phoneno']
        address= request.POST['address']
        pincode= request.POST['pincode']
        bio= request.POST['bio']
        
        profile.phonenumber= phonenumber
        profile.address= address
        profile.pincode= pincode
        profile.bio= bio
        profile.save()
        print('saved')
        redirect('/')
    return render(request, 'edit_profile.html', {'user':user})