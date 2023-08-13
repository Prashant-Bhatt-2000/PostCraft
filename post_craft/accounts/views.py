from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login
from .models import User

# Create your views here.


def Register(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not user or not email or not password: 
            messages.error(request, "Please fill the form for registeration.")
        else: 
            user_exist = User.objects.filter(email=email).exists()

            if user_exist: 
                messages.error(request, "Please Login ! email already exists")
            else: 
                password_hash = make_password(password)

                user = User(user=user, email=email, password=password_hash)

                user.save()
                messages.success(request, "User Successfully Registered")

        print(f'username : {user}, email: {email}, password: {password}')
    return render (request, 'register.html')



def loginuser(request): 
    if request.method == "POST":
        email = request.POST.get('loginemail')
        password = request.POST.get('loginpassword')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User Not Found')
            return render(request, 'login.html')
        
        password_correct = check_password(password, user.password)

        if password_correct:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('/')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html')

    return render(request, 'login.html')
