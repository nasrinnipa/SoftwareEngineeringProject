from django.db import models

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=20)

class Product(models.Model):

    id= models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(default='')

    def __str__(self):
        return self.product_name

class User(models.Model):

    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=20)

    