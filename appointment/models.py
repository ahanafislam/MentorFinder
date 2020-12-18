from django.db import models
from datetime import datetime

class Appointment(models.Model):
    mentor_title = models.CharField(max_length=500)
    mentor_id = models.IntegerField()
    mentor_Name = models.CharField(max_length=200, blank=True, null=True)
    mentor_category = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    apply_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    user_id = models.IntegerField(blank=True)
    visiting_free = models.FloatField(default=None, blank=True)
    done_job = models.BooleanField(default=False)
    is_visited = models.BooleanField(default=False)
    appointment_date = models.DateTimeField(max_length=200, default=None, blank=True, null=True)
    mentor_username = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.name

    def apply_date_pretty(self):
            return self.apply_date.strftime('%d-%m-%Y')

    def appointment_date_pretty(self):
            return self.appointment_date.strftime('%d-%m-%Y at %I:%M %p')