from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout

from .Buyer_Form import *
from .Seller_Form import *
# Create your views here.

def home(request):
    return render(request, "Home.html")

def logout(request):
    auth_logout(request)
    return render(request, "Sign_In.html")


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('/seller')
            else:
                return redirect('/market')
        else:
            return render(request, 'Sign_In.html', {'error': 'Username or password incorrect'})
    
    return render(request, "Sign_In.html")


def sign_up(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        role = request.POST.get('role')  # This will get the selected role (Buyer or Seller)

        # Check if passwords match
        if password != password_confirm:
            return render(request, 'Sign_Up.html', {'error': 'Passwords do not match'})
        
        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'Sign_Up.html', {'error': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'Sign_Up.html', {'error': 'Email already exists'})
        
        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name

        # Set is_admin or is_staff based on role selection
        if role == 'Seller':
            user.is_superuser = True  # Set admin to True if role is Seller
        elif role == 'Buyer':
            user.is_staff = True  # Set staff to True if role is Buyer

        user.save()

        # Redirect to Sign In page
        return render(request, "Sign_In.html")
        
    return render(request, "Sign_Up.html")


def buyer(request):
    user = request.user
    return render(request, template_name='Buyer.html', context={'user': user})

def add_Buyer(request):
        form = Buyer_Form()

        if form.is_valid():
            form.save()
            return redirect('buyer')
        context = {
            'form':form,
        }
        return render(request, template_name='add_buyer.html', context=context)

def buyer(request):
    user = request.user
    return render(request, template_name='Buyer.html', context={'user': user})

def add_Seller(request):
        form = Seller_Form()


        if form.is_valid():
            form.save()
            return redirect('seller')
        context = {
            'form': form,
        }
        return render(request, template_name='add_seller.html', context=context)


def inventory(request):
    inventory = Inventory.objects.all()
    context = {
        'inventory':inventory,
    }
    return render(request, template_name='Inventory.html', context=context)

def market(request):
    products = Product.objects.all()
    return render(request, 'market.html', {'products': products})
def productDetails(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product-details.html', {'product': product})
def addToCart(request, product_id):
    buyer_id = request.user.id or 1 # default
    cart = Cart.objects.create(buyer_id=buyer_id, product_id=product_id)
    product = get_object_or_404(Product, pk=product_id)
    
    messages.success(request, f"Product '{product.product_name}' added to cart successfully!")

    # return render(request, 'product-details.html', {'product': product})
    return redirect("market")
def showCart(request):
    buyer_id = request.user.id or 1 # default
    cart = Cart.objects.filter(buyer_id=buyer_id)
    products = []
    for cart_item in cart:
        product = Product.objects.get(id=cart_item.product_id)
        products.append(product)

    return render(request, 'cart.html', {'cart': cart, 'products':products})

def checkout(request):
    buyer_id = request.user.id or 1 # default
    cart = Cart.objects.filter(buyer_id=buyer_id)
    products = []
    totalPrice = 0
    totalItems = 0
    for cart_item in cart:
        product = Product.objects.get(id=cart_item.product_id)
        products.append(product)
        totalPrice += product.price
        totalItems += 1

    return render(request, 'checkout.html', {'total': totalPrice, 'products':products})
def checkoutMake(request):
    buyer_id = request.user.id or 1 # default
    cart = Cart.objects.filter(buyer_id=buyer_id)
    products = []
    totalPrice = 0
    totalItems = 0
    for cart_item in cart:
        product = Product.objects.get(id=cart_item.product_id)
        order = Order.objects.create(Buyer_Id=buyer_id, Seller_Id=1, Product_Id=product, Product_Amount=product.price)
    
    # clear cart 
    cart.delete()
    orders = Order.objects.filter(Buyer_Id=buyer_id)
    messages.success(request, f"Order Placed Successfully!")
    return redirect('https://epay-gw.sslcommerz.com/afc8feb0823dc280a37f80611cf36058e37dce8f')

    return render(request, 'order.html', {'orders': orders})
def showOrders(request):
    buyer_id = request.user.id or 1 # default

    orders = Order.objects.filter(Buyer_Id=buyer_id)
    return render(request, 'order.html', {'orders': orders})
