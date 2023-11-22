from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
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
