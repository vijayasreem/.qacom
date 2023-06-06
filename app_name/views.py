# views.py

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse

@csrf_exempt
def register_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    encrypted_pwd = make_password(password)

    user = User.objects.create_user(
        username=username,
        password=encrypted_pwd
    )
    user.save()

    return HttpResponse("Registration successful!")

@csrf_exempt
def change_password(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    encrypted_pwd = make_password(password)

    user = User.objects.get(username=username)
    user.password = encrypted_pwd
    user.save()

    return HttpResponse("Password changed successfully!")

@csrf_exempt
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Login successful!")
    else:
        return HttpResponse("Invalid username or password!")