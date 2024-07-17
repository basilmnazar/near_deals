from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from deal_app.models import*
from datetime import time
# from django.core.mail import send_mail
from django.contrib.auth import authenticate,login as auth_login,logout,login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dealer_index(request):
    dealerdatas = register_dealer.objects.all()
    return render(request, 'dealer_index.html', {'dealerdatas': dealerdatas})
    

# views for registration /////////////

def deal_register(request):
    if request.method == 'POST':
        merchant_name = request.POST['merchant_name']
        merchant_type = request.POST['merchant_type']
        merchant_address = request.POST['merchant_address']
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

            return render(request,'deal_register.html')
        else:
            if (password != cpassword):
                print('password is not match')
                return render(request,'deal_register.html')
            else:
                 #create a new user
                user=User.objects.create_user(
                                          email=email,
                                          password=password,
                                          username=user_name
                                          )

                user.save()

                newdealer=register_dealer(user=user,phone=phone,merchant_type=merchant_type,city=city,merchant_name=merchant_name,merchant_address=merchant_address)
                newdealer.save()
                print("success")

                auth_login(request, user)
                return redirect('dealer_login')
           

    else:
        print('not registered')
        return render(request,'deal_register.html')    

            
# views for login page///////

def dealer_login(request):
    if request.method == 'POST':
        username=request.POST['uname']
        password=request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dealer_index')
        else:
            return render(request,'dealer_login.html')
    else:
        
        return render(request,"dealer_login.html")


#forgot password///////

def forgot_password(request):

    return render(request,'password_reset_done.html')

    
    #logout

def admin_logout(request):
    logout(request)
    return redirect("dealer_login")

def index_main(request):
    items = model_add_fields.objects.all()
    return render(request, 'index_main.html', {'items': items})


# views for add field..../

from datetime import datetime
from django.shortcuts import render, redirect
from .models import model_add_fields

def add_fields(request):
    if request.method == 'POST':
        # Extract data from the request
        item_name = request.POST.get('item-name')
        description = request.POST.get('description')
        start_time_str = request.POST.get('time-from')
        end_time_str = request.POST.get('time-to')
        item_img = request.FILES.get('image')

        # Basic validation (optional)
        if not item_name or not description or not start_time_str or not end_time_str:
            return render(request, 'add_fields.html', {'message': 'Please fill in all required fields'})

        # Try converting time strings to time objects
        try:
            start_time = datetime.strptime(start_time_str, '%H:%M').time()  # Parse time in HH:MM format
            end_time = datetime.strptime(end_time_str, '%H:%M').time()
        except ValueError:
            # Handle invalid time format
            return render(request, 'add_fields.html', {'message': 'Invalid time format. Use HH:MM format.'})

        # Create a new model object
        try:
            new_field = model_add_fields.objects.create(
                item_name=item_name, description=description, start_time=start_time, end_time=end_time, item_img=item_img)
            return redirect('index_main')  # Redirect to index_main after successful creation
        except Exception as e:  # Handle potential exceptions
            return render(request, 'add_fields.html', {'message': f'Error adding item: {str(e)}'})

    else:
        return render(request, 'add_fields.html', {'message': 'Invalid request method'})
