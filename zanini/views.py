from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout

def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def menu_items(request):
    return render(request, 'menu_items.html')

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'Signup success!')
            return redirect('home')
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],)
            if user is not None:
                login(request, user)
                messages.success(request, "You're logged in!")
                return redirect('home')
    return render(request, "login.html", {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You're logged out!")
    return redirect('home')
