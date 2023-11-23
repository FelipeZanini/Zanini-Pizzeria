import datetime
from django.test import TestCase
from .models import Reservation
from .forms import ReservationForm

class ReservationFormTest(TestCase):

    def test_form_valid_data(self):
        form_data = {
            'table_size': 4,
            'booking_time': '18:00',
            'date': datetime.date.today(),
        }
        form = ReservationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {
            'table_size': 'invalid_size', 
            'booking_time': '25:00',      
            'date': 'invalid_date',   
        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())

  def test_form_invalid_date_in_past(self):
        # Test if the form is invalid when the date is in the past
        past_date = datetime.date.today() - datetime.timedelta(days=7)
        form_data = {
            'table_size': 3,
            'booking_time': '19:00',
            'date': past_date,
        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

    def test_form_table_size_choices(self):
        # Test if the table size choices match the expected values
        form = ReservationForm()
        table_size_choices = form.fields['table_size'].widget.choices
        expected_choices = Reservation.TABLE_SIZE_CHOICES
        self.assertEqual(table_size_choices, expected_choices)

class LoginFormTest(TestCase):

    def test_form_valid_data(self):
        form_data = {
            'username': 'user123',
            'password': 'pass12354421p',
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