from django.contrib import admin

from .models import Admin, Product, User

admin.site.register(Admin)
admin.site.register(Product)
admin.site.register(User)
