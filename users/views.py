from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)

        # Assign user to a group based on role
        if role == 'seller':
            group, _ = Group.objects.get_or_create(name='Sellers')
        else:
            group, _ = Group.objects.get_or_create(name='Buyers')
        user.groups.add(group)
        user.save()

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'signup.html')


@login_required
def home(request):
    user = request.user
    role = None
    if user.groups.filter(name='Sellers').exists():
        role = 'seller'
    elif user.groups.filter(name='Buyers').exists():
        role = 'buyer'
    else:
        role = 'guest'

    return render(request, 'home.html', {'role': role})




@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  

