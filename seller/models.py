from django.db import models

from dashboard.models import Product

class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=20)



class Order(models.Model):
    id = models.AutoField(primary_key=True)
    sellerid =models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True, null=True)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    update_date = models.DateTimeField(auto_now_add=True,auto_now=False)


class Payment(models.Model):
    id= models.AutoField(primary_key=True)
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    update_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    Transaction_option = (
        ('Bkash','Bkash'),
        ('Rocket', 'Rocket'),
        ('Nagad', 'Nagad'),
        ('pay_on_delivery', 'pay_on_delivery'),
    )
    transaction =models.CharField(max_length=100, choices=Transaction_option,blank=True, null= True)