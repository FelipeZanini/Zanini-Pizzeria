from django.db import models
from django.contrib.auth.models import User



class Reservation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(null=False)

    TABLE_SIZE = [
        ("2", "Table for two"),
        ("4", "Table for four"),
        ("6", "Table for six"),
    ]

    BOOKING_TIME = [
        ("2", " 2pm to 3pm"),
        ("3", " 3pm to 4pm"),
        ("4", " 4pm to 5pm"),
        ("5", " 5pm to 6pm"),
        ("6", " 6pm to 7pm"),
        ("7", " 7pm to 8pm"),
        ("8", " 8pm to 9pm"),
    ]

    booking_time = models.CharField(max_length=1, choices=BOOKING_TIME, null=False)
    table_size = models.CharField(max_length=1, choices=TABLE_SIZE)