from django.contrib import admin

# Register your models here.
from .models import Seller, Order, Payment

admin.site.register(Seller)
admin.site.register(Order)
admin.site.register(Payment)
