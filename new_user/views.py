from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method=='POST':
        first_name = request.POST['FirstName']
        last_name = request.POST['LastName']
        user_name = request.POST['Username']
        email = request.POST['Email']
        password = request.POST['Password1']
        confirm_password = request.POST['Password2']

        isuser=True
        isemail=True
        isfirst_name=True
        islast_name=True
        ispassword=True

        if len(first_name)==0:
            messages.info(request,'first name is empty')
            isfirst_name=False

        if len(last_name)==0:
            messages.info(request,'last name is empty')
            islast_name=False

        if len(user_name)==0:
            messages.info(request,'username is empty')
            isuser=False
                         
        if len(email)==0:
            messages.info(request,'email is empty')
            isuser=False

        if len(password)<8:
            ispassword=False
            messages.info(request,'Password is short')

        if not isuser and not isemail and not isfirst_name and not islast_name and not ispassword:
            return redirect('register')

        else:
            if password == confirm_password:
                isUser=True
                isEmail=True
                if User.objects.filter(username=user_name).exists():
                    isUser=False
                if User.objects.filter(email=email).exists():
                    isEmail=False

                if isemail and isuser:                
                    user = User.objects.create_user(username=user_name,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    print('user created')
                    return redirect('/')
                else:
                    if not isUser:
                        messages.info(request,'Username Taken')
                
                    if not isEmail:
                        messages.info(request,'Email already present')

                    return redirect('register')

            else:
                print('wrong password')
                return redirect('register')
                   

    else:
        return render(request,'registration/signup.html')


def login(request):
    if request.method=='POST':
        username = request.POST['Username']
        password = request.POST['Password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'registration/login.html')


def logout(request):
    auth.logout(request)
    return  redirect('/')