import datetime
from datetime import date
from django.contrib.auth.models import User
from .models import Reservation
from .forms import ReservationForm
from .forms import LoginForm

from django.test import TestCase
from django.test import Client

from django.urls import reverse

class ReservationFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            'table_size': '4',
            'booking_time': '8',
            'date': datetime.date.today(),
        }
        form = ReservationForm(data=form_data)
        self.assertTrue(form.is_valid())
    def test_form_invalid_data(self):
        form_data = {
            'table_size': '8',
            'booking_time': '5',
            'date': 's21',
        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())

class LoginFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            'username': 'user1',
            'password': 'pass1',
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
    def test_form_invalid_data(self):
        form_data = {
            'username': '',
            'password': '',
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password', form.errors)

    
class BookTableTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass1')
        self.client = Client()
    def test_book_table_authenticated_user(self):
        self.client.login(username='user1', password='pass1')
        form_data = {
            'table_size': '4',
            'booking_time': '8',
            'date': '2023-12-01',
        }
        response = self.client.post(reverse('book_table'), form_data)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(Reservation.objects.count(), 1)
    def test_book_table_invalid_data(self):
        self.client.login(username='user1', password='pass1')
        form_data = {
            'table_size': '9',
            'booking_time': '68',
            'date': 'date342s',
        }
        response = self.client.post(reverse('book_table'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Reservation.objects.count(), 0)

    def test_book_table_full_tables(self):
        self.client.login(username='user1', password='pass1')
        Reservation.objects.create(table_size='4', booking_time='5', date='2023-12-01', user=self.user)
        form_data = {
            'table_size': '4',
            'booking_time': '5',
            'date': '2023-12-01',
        }
        response = self.client.post(reverse('book_table'), form_data)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('book_table'))
        self.assertEqual(Reservation.objects.count(), 1)

    def test_book_table_one_reservation_at_a_time(self):
        self.client.login(username='user1', password='pass1')
        Reservation.objects.create(table_size='2', booking_time='8', date='2023-12-01', user=self.user)
        form_data = {
            'table_size': '2',
            'booking_time': '8',
            'date': '2023-12-02',
        }
        response = self.client.post(reverse('book_table'), form_data)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('book_table'))
        self.assertEqual(Reservation.objects.count(), 1)