from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_details(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1) # male = m, female = f, other = o
    dob = models.DateField()
    contact_no = models.IntegerField()
    contact_sharing = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user')

class Cab(models.Model):
    source = models.CharField(max_length=20) 
    destination = models.CharField(max_length=20)
    dep_date_time = models.DateTimeField()
    size = models.IntegerField()
    cab_admin = models.ForeignKey(User,on_delete = models.CASCADE,related_name='cab_admin')
    created_at = models.DateTimeField(auto_now_add=True)

class Passengers(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name='passangers')
    of_cab = models.ForeignKey(Cab,on_delete = models.CASCADE, related_name='of_cab')
    is_cab_admin = models.BooleanField()
    approval_status = models.CharField(max_length=1) # requested = r, approved = a, declined = d

    