from django.db import models
from django.contrib.auth.models import User

from dashboard.models import Product

class Seller(models.Model):
    
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=20)


def __str__(self):
    return self.firstname


