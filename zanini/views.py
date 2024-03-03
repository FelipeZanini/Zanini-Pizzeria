from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm, ReservationForm
from .models import Reservation


def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def book_table(request):
    # if not request.user.is_authenticated:
    #     messages.success(request, 'Login for table reservations!')
    #     return redirect('login')

    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            table_size = form.cleaned_data.get("table_size")
            booking_time = form.cleaned_data.get("booking_time")
            dt = form.cleaned_data.get("date")
            if Reservation.check_table_avaliability(table_size, booking_time,
                                                    dt):
                reservation = Reservation(table_size=table_size,
                                          booking_time=booking_time,
                                          date=dt)
                if not Reservation.objects.filter(user=request.user).exists():
                    if reservation.date >= date.today():
                        reservation.user = request.user
                        reservation.save()
                        messages.success(request, 'Table booked successfully!')
                        return redirect('home')
                    else:
                        messages.success(request,
                                         "You can't time travel, yet.")
                        return redirect('book_table')
                else:
                    messages.success(request,
                                     'One reservation at a time allowed!')
                    return redirect('book_table')
            else:
                messages.success(request,
                                 'Sorry, Tables full for this date and time.')
                return redirect('book_table')
    Reservation.delete_old_dates()
    return render(request, 'book_table.html', {'form': form})


@login_required
def delete_reservation(request, id_item):
    reservation = Reservation.objects.get(id=id_item, user=request.user)
    print(reservation)
    if not reservation.date == date.today():
        reservation.delete()
        messages.success(request, 'Reservation canceled!')
        return redirect('user_page')
    messages.success(request, "Sorry, same day cancellations not allowed.")
    return redirect('user_page')


@login_required
def update_reservation(request, id_item):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = Reservation.objects.get(id=id_item,
                                                  user=request.user)
            reservation.table_size = form.cleaned_data.get("table_size")
            reservation.booking_time = form.cleaned_data.get("booking_time")
            reservation.date = form.cleaned_data.get("date")
            if Reservation.check_table_avaliability(reservation.table_size,
                                                    reservation.booking_time,
                                                    reservation.date):
                reservation.save()
                messages.success(request, 'Reservation updated!')
                return redirect('home')
            else:
                messages.success(request,
                                 'Sorry, Tables full for this date and time.')
    return render(request, 'book_table.html', {'form': form})


# @login_required
def user_page(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'user_page.html', {'reservations': reservations})


def menu_items(request):
    return render(request, 'menu_items.html')


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


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You're logged out!")
    return redirect('home')


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


@login_required
def delete_account(request):
    user = request.user
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('home')
