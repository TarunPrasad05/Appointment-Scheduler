from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


TIME_CHOICES = (
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user2 = models.CharField(User, null=True, max_length=30)
    day = models.DateField(default=datetime.now)
    title = models.CharField(max_length=20, default="No Title")
    agenda = models.CharField(max_length=100, default="No Agenda")
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="10 AM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"