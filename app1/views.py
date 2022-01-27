from email.policy import HTTP
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from matplotlib.pyplot import title
from app1.forms import UserForm
from django.contrib import *
from django.contrib import messages
from app1.models import *
from random import randrange
from django.conf import settings
from django.core.mail import EmailMessage,send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.



# for user registration (new)
def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            print("Existsss")
            messages.error(
            request,
            "User already exists",
            extra_tags="alert alert-error alert-dismissible show",)
            return render(request,'register.html')

        else:
            global temp 
            temp = {
                'email' : email,
                'fname' : fname,
                'lname' : lname,
                'username' : username,
                'password' : password1,
                }

            otp = randrange(1000,9999)
            subject = otp
            message = f'Hi your otp for Reset password is {otp}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'verify-otp.html',{'otp':otp})
        # messages.success(request, "Your account has been successfully created.")
        return redirect('otp')

    return render(request,'register.html')



# for user login (new)
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)
        print("alis")
        if user:
            return redirect('home')
            # return render(request, "home.html")
        else:
            
            messages.error(request, "Enter Proper Details!")
            # return redirect('login')
            return render(request, "login.html")

    return render(request, "login.html")



# for OTP verification (new)
def otp(request):
    if request.method == "POST":
        otp = request.POST['otp']
        uotp = request.POST['uotp']
        if otp == uotp:
            global temp
            myuser = User.objects.create_user(
            username = temp["username"],
            first_name = temp["fname"],
            last_name = temp["lname"],
            email = temp["email"],
            password = temp["password"],
            )

            myuser.save()
            return render(request,'login.html')
    else:
        return render(request,'verify-otp.html')



# for logout (new)
def logout_user(request):
    logout(request)
    return render(request, "logout_user.html")



# @login_required(login_url="index")
@login_required(login_url="login")
def home(request):
    return render(request,'home.html')


  
# @login_required(login_url="index")
@login_required(login_url="login")
def usa(request):
    return render(request,'usa.html')
    


# for feedback form
@login_required(login_url="login")
def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        print(name,email,desc)
        Feedback.objects.create(
            name = name,
            email = email,
            desc = desc,
        ).save()
    return render(request, 'home.html')



# for application form
@login_required(login_url="login")
def form(request):
    if request.method == "POST":
        choice = request.POST.get('choice')
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        university = request.POST.get('university')
        cgpa = request.POST.get('cgpa')
        ielts = request.POST.get('ielts')
        Form.objects.create(
            choice = choice,
            name = name.upper(),
            email = email,
            number = number,
            university = university,
            cgpa = cgpa,
            ielts = ielts,
        ).save()
        return render(request, 'usa.html')
    else:
        choice=request.GET.get("PU")
        return render(request, 'form.html',{"choice":choice})



# for search
def search(request):
    # print("dsfds")
    username=request.POST.get("query")
    # count = Form.objects.filter(name=username).count()
    # print(count)
    if username.isupper():
        results = Form.objects.filter(name=username)
    else:
        results = Form.objects.filter(name=username.upper())
    return render(request, 'usa.html',{"res":results})