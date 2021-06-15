from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.warning(request, 'Username already exists')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exists')
                return redirect('signup')

            else:
                user = User.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                username=user_name,
                                                email=email,
                                                password=password)
                user.save()
                messages.success(request, "Account created successfully")
                return redirect('login')

        else:
            messages.warning(
                request, 'Password and Confirm password has to be same')
            return redirect('register')

    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('/')
        else:
            messages.warning(request, 'Please enter valid credentials')
            return redirect('login')

    return render(request, 'accounts/signin.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'Log out successful')
    return redirect('/')
