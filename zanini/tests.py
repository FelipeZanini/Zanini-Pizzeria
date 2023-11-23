import datetime
from django.test import TestCase
from .models import Reservation
from .forms import ReservationForm

class ReservationFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            'table_size':'4',
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
    def test_form_table_size_choices(self):
        form = ReservationForm()
        table_size_choices = form.fields['table_size'].widget.choices
        expected_choices = Reservation.TABLE_SIZE_CHOICES
        self.assertEqual(table_size_choices, expected_choices)

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
        self.assertContains(response, 'This field is required.')  
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
        self.assertContains(response, 'Sorry, Tables full for this date and time.')
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
        self.assertContains(response, 'One reservation at a time allowed.')
        self.assertEqual(Reservation.objects.count(), 1)

class CheckTableAvailabilityTest(TestCase):
    def test_table_available(self):
        Reservation.objects.create(table_size='4', booking_time='6', date=date(2023, 12, 1))
        result = Reservation.check_table_availability('4', '6', date(2023, 12, 1))
        self.assertTrue(result)
    def test_table_unavailable(self):
        Reservation.objects.create(table_size='2', booking_time='5', date=date(2023, 12, 1))
        Reservation.objects.create(table_size='2', booking_time='5', date=date(2023, 12, 1))
        result = Reservation.check_table_availability(2, '18:00', date(2023, 12, 1))
        self.assertFalse(result)

class DeleteReservationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass1')
        self.reservation = Reservation.objects.create(
            user=self.user,
            date=timezone.now().date()
        )
    def test_delete_reservation(self):
        self.client.login(username='user1', password='pass1')
        url = reverse('user_page')
        response = delete_reservation(self.client.request(), id_item=self.reservation.id)
        self.assertEqual(response.url, url)
        self.assertEqual(response.status_code, 302) 

        with self.assertRaises(Reservation.DoesNotExist):
            Reservation.objects.get(id=self.reservation.id)
    def test_cancel_same_day_reservation(self):
        self.client.login(username='user1', password='pass1')
        self.reservation.date = date.today()
        self.reservation.save()
        response = delete_reservation(self.client.request(), id_item=self.reservation.id)
        self.assertEqual(response.url, reverse('user_page'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Reservation.objects.filter(id=self.reservation.id).exists())
        self.assertContains(response, "Sorry, same day cancellations not allowed.")