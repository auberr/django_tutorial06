from django.shortcuts import render, redirect
from user.models import User
from django.contrib.auth import authenticate, login as loginsession

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        User.objects.create_user(username=username, password=password, phone=phone, address=address)
        print(username, password)
        return redirect('user:login')
    
    else:
        return '잘못된 접속입니다.'

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(username, password)
            loginsession(request, user)
            return redirect('user:home')
        
        else:
            return redirect('user:signup')
    

def home(request):
    # if request.user.is_authenticated:
    #     return render(request, 'home.html')
    # else:
    #     return redirect('user:login')

    user = request.user
    users = User.objects.all()
    if user in users:
        return render(request, 'home.html')
    elif request.user is not users:
        return redirect('user:login')
        