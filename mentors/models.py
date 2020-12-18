from django.db import models
from django.contrib.auth import get_user_model
from employee.models import Employee
from datetime import datetime
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from .choices_tpl import divisions_list, district_list, category, sex


User = get_user_model()

class Mentor(models.Model):
        added_by = models.CharField(max_length=200,blank=True, null=True)
        mentor_Name = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        professional_degree = models.CharField(max_length=200)
        designation = models.CharField(max_length=200, blank=True)
        specialist_in = models.CharField(max_length=200, blank=True)
        visiting_houre = models.CharField(max_length=200, blank=True)
        visiting_fees = models.CharField(max_length=200)
        descriptions = models.TextField(blank=True)
        sex = models.CharField(max_length=50, default=None, blank=True, choices=sex)
        nid_no = models.CharField(max_length=200,blank=True)
        catagory = models.CharField(max_length=300, default=None, blank=True, choices=category)
        chamber_address = models.CharField(max_length=300,blank=True)
        district = models.CharField(max_length=300, default=None, blank=True, choices=district_list)
        divisions = models.CharField(max_length=300, default=None, blank=True, choices=divisions_list)
        name = models.CharField(max_length=200, null=True, blank=True)
        mentors_picture = models.ImageField(upload_to='photos/dp/mentors/%Y/%m/%d/',blank=True)
        cover_photo_1 = models.ImageField(upload_to='photos/mentors/cover/%Y/%m/%d/',blank=True)
        cover_photo_2 = models.ImageField(upload_to='photos/mentors/cover/%Y/%m/%d/',blank=True)
        cover_photo_3 = models.ImageField(upload_to='photos/mentors/cover/%Y/%m/%d/',blank=True)
        join_date = models.DateTimeField(default=datetime.now, blank=True)
        is_published = models.BooleanField(default=True)
        score = models.IntegerField(default=0, validators=[ MaxValueValidator(5), MinValueValidator(0),])


        def __str__(self):
            return f"{self.mentor_Name}"

        def summary(self):
            return self.descriptions[:150]

        def pub_date_pretty(self):
            return self.pub_date.strftime('%d %B %Y')
