from django.contrib import admin
from .models import Seller, Buyer, Product, Sell_Product, Order, Inventory, Payment

# Register your models here.

admin.site.register([Seller, Buyer, Sell_Product, Order, Inventory, Payment])