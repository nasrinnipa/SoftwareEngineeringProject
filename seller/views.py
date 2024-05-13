from django.shortcuts import render,redirect
from django.http import HttpResponse


from .models import Seller

def seller(request):
    seller = Seller.objects.all()
    return render(request, 'seller.html', {'seller': seller})
