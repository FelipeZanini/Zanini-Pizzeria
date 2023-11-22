from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm, ReservationForm
from .models import Reservation

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

def book_table(request):
    if not request.user.is_authenticated:
        messages.success(request, 'Login for table reservations!')
        return redirect('login')

    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            ts = form.cleaned_data.get("table_size")
            bt = form.cleaned_data.get("booking_time")
            dt = form.cleaned_data.get("date")
            if Reservation.check_table_avaliability(ts, bt, dt):
                reservation = Reservation(table_size=bt,
                                          booking_time=bt, date=dt)
                if not Reservation.objects.filter(user=request.user).exists():
                    reservation.user = request.user
                    reservation.save()
                    messages.success(request, 'Table booked successfully!')
                    return redirect('home')
                messages.success(request, 'One reservation at a time allowed!')
                return redirect('book_table')
            messages.success(request,
                             'Sorry, Tables full for this date and time.')
            return redirect('book_table')
    return render(request, 'book_table.html', {'form': form})
