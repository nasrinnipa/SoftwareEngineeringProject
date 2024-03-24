from django.contrib import admin


# Register your models here.
from .models import Buyer,Order,Payment

admin.site.register(Buyer)
admin.site.register(Order)
admin.site.register(Payment)

