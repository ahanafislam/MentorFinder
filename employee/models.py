from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


class Employee(models.Model):
    employee_name = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"{self.employee_name.first_name} {self.employee_name.last_name} "