from django.shortcuts import render, get_object_or_404

from .models import Product,User

def home(request):
    return render(request, 'dashboard.html')

def product(request):
    products = Product.objects.all()

    return render(request, 'products/index.html', {'products': products})
def showProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/show.html', {'product': product})
def user(request):
    users = User.objects.all()

    return render(request, 'users/index.html', {'users': users})