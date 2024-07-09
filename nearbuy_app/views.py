from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from nearbuy_app.models import*
from django.contrib.auth import authenticate,login as auth_login,logout,login

# Create your views here.


def admin_index(request):
    return render(request, "admin_index.html")

# views for registration /////////////

def admin_register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        gender = request.POST['gender']
        state = request.POST['state']
        city = request.POST['city']
        phone=request.POST['phone']
        user_name= request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        print(user_name)

#check if the  username is unique

        if User.objects.filter(username=user_name):
            print('username is already exists') 

            return render(request,'admin_register.html')
        else:
            if (password != cpassword):
                print('password is not match')
                return render(request,'admin_register.html')
            else:
                 #create a new user
                user=User.objects.create_user(first_name=first_name,
                                          last_name=last_name,
                                          email=email,
                                          password=password,
                                          username=user_name
                                          )

                user.save()

                newuser=register_user(user=user,phone=phone,gender=gender,state=state,city=city)
                newuser.save()
                print("success")

                auth_login(request, user)
                return redirect('admin_login')
           

    else:
        print('not registered')
        return render(request,'admin_register.html')    

            
# views for login page///////

def admin_login(request):
    if request.method == 'POST':
        username=request.POST['uname']
        password=request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_index')
        else:
            return render(request,'admin_login.html')
    else:
        
        return render(request,"admin_login.html")


