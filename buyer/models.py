from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Product
# Create your models here.

class Seller(models.Model):

    Seller_Id = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Date_Of_Birth = models.CharField(max_length=100, blank=True, null=True)
    Location = models.CharField(max_length=100)
    Phone_Number = models.IntegerField(null=True)
    Email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.First_Name

class Buyer(models.Model):

    Buyer_Id = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Date_Of_Birth = models.CharField(max_length=100, blank=True, null=True)
    Location = models.CharField(max_length=100)
    Phone_Number = models.IntegerField(null=True)
    Email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.First_Name

class Sell_Product(models.Model):

    Seller_Id = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    Product_Id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

class Order(models.Model):
    Order_Id = models.AutoField(primary_key=True)
    Buyer_Id = models.IntegerField(null=True)
    Seller_Id = models.IntegerField(null=True)
    Order_Date = models.DateTimeField(auto_now_add=True)
    Total_Amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # Other fields as necessary

    def __str__(self):
        return f"Order {self.Order_Id} by Buyer {self.Buyer_Id}"


class OrderItem(models.Model):
    Order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate the subtotal each time an OrderItem is saved
        self.Subtotal = self.Product.price * self.Quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Quantity} x {self.Product.product_name} in Order {self.Order.Order_Id}"

class Inventory(models.Model):

    Product_Id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    Seller_Id = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    Product_Price = models.IntegerField(null=True)
    Product_Amount = models.IntegerField(null=True)

class Payment(models.Model):

    Payment_Id = models.AutoField(primary_key=True)
    Order_Id = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    Payment_Amount = models.IntegerField(null=True)
    set_choice = (
        ('Bkash', 'Bkash' ),
        ('Rocket', 'Rocket'),
        ('Nogod', 'Nogod'),

    )

    Payment_Option = models.CharField(max_length=100, choices=set_choice, null=True)
    Payment_Time = models.TimeField(auto_now_add=True, auto_now=False)
    Payment_Date = models.DateTimeField(auto_now_add=True, auto_now=False)

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    buyer_id = models.IntegerField(null=True)
    product_id = models.IntegerField(null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Buyer {self.buyer_id} - Product {self.product_id} (x{self.quantity})"