from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, "Home.html")

def sign_in(request):
    return render(request, "Sign_In.html")

def sign_up(request):
    return render(request, "Sign_Up.html")

def buyer(request):
    buyer = Buyer.objects.all()
    context = {
        'buyer': buyer,
    }
    return render(request, template_name='Buyer.html', context=context)

def seller(request):
    seller = Seller.objects.all()
    context = {
        'seller': seller,
    }
    return render(request, template_name='Seller.html', context=context)



def inventory(request):
    inventory = Inventory.objects.all()
    context = {
        'inventory':inventory,
    }
    return render(request, template_name='Inventory.html', context=context)

