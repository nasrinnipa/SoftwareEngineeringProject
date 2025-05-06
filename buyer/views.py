from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import *
from django.contrib.auth.models import User

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.template.loader import render_to_string

# for pdf 
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template

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
                return redirect('/product')
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

@login_required
def market(request):
    products = Product.objects.all()
    return render(request, 'market.html', {'products': products})

@login_required
def productDetails(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product-details.html', {'product': product})

@login_required
def addToCart(request):
     if request.method == "POST":
        buyer_id = request.user.id or 1  # Replace this logic with actual user handling
        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity", 1))

        product = get_object_or_404(Product, pk=product_id)

        # Optional: check if enough stock is available
        if quantity > product.quantity:
            messages.error(request, f"Only {product.quantity} kg available.")
            return redirect(f"/market/product-details/{product_id}")

        # Check if the product is already in the cart
        cart_item, created = Cart.objects.get_or_create(buyer_id=buyer_id, product_id=product.id)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()

        messages.success(request, f"{quantity} kg of {product.product_name} added to your cart!")
        return redirect("market")

@login_required
def showCart(request):
    buyer_id = request.user.id or 1  # default to 1 if no user is logged in
    cart_items = Cart.objects.filter(buyer_id=buyer_id)
    products = []
    total_cost = 0  # Variable to hold the total cost of items in the cart
    
    for cart_item in cart_items:
        product = Product.objects.get(id=cart_item.product_id)
        cart_item.product = product
        cart_item.total_price = cart_item.quantity * product.price  # Calculate total price for each cart item
        total_cost += cart_item.total_price  # Add item price to total cost
        products.append(cart_item)

    return render(request, 'cart.html', {'cart_items': cart_items, 'products': products, 'total_cost': total_cost})

@login_required
def remove_from_cart(request, item_id):
    try:
        cart_item = Cart.objects.get(id=item_id, buyer_id=request.user.id)
        cart_item.delete()
        messages.success(request, "Product removed from cart successfully.")
    except Cart.DoesNotExist:
        messages.error(request, "Product not found in your cart.")

    return redirect('/cart')  # Redirect back to the cart page

@login_required
def checkout(request):
    buyer_id = request.user.id or 1 # default
    cart = Cart.objects.filter(buyer_id=buyer_id)
    products = []
    totalPrice = 0
    totalItems = 0
    products_with_totals = []
    for cart_item in cart:
        product = Product.objects.get(id=cart_item.product_id)
        quantity = cart_item.quantity
        total = product.price * quantity

        products_with_totals.append({
            'product': product,
            'quantity': quantity,
            'total': total,
        })

        totalPrice += total
        totalItems += quantity

    return render(request, 'checkout.html', {
        'total': totalPrice,
        'products': products_with_totals
    })

@login_required
def checkoutMake(request):
    buyer_id = request.user.id or 1  # default
    cart = Cart.objects.filter(buyer_id=buyer_id)
    totalPrice = 0
    totalItems = 0

    # Create a new order
    order = Order.objects.create(Buyer_Id=buyer_id, Seller_Id=1)

    # Process each item in the cart
    for cart_item in cart:
        product = Product.objects.get(id=cart_item.product_id)
        quantity = cart_item.quantity
        subtotal = product.price * quantity

        # Create an OrderItem for each product in the cart
        OrderItem.objects.create(
            Order=order,
            Product=product,
            Quantity=quantity,
            Subtotal=subtotal
        )

        # Deduct the product quantity from stock
        if product.quantity >= quantity:
            product.quantity -= quantity
            product.save()
        else:
            messages.error(request, f"Not enough stock for {product.product_name}.")
            return redirect('cart')  # Redirect back to the cart in case of insufficient stock

        # Add the subtotal to the total price
        totalPrice += subtotal
        totalItems += quantity

    # Update the total amount for the order
    order.Total_Amount = totalPrice
    order.save()

    # Clear the cart after order creation
    cart.delete()

    # Redirect to the payment gateway (or any other page)
    messages.success(request, f"Order Placed Successfully! Total Items: {totalItems}")
    # return redirect('https://epay-gw.sslcommerz.com/afc8feb0823dc280a37f80611cf36058e37dce8f')

    # render the order confirmation page
    return redirect('/order')

@login_required
def showOrders(request):
    buyer_id = request.user.id or 1  # default

    orders = Order.objects.filter(Buyer_Id=buyer_id).order_by('-Order_Id')
    return render(request, 'order.html', {'orders': orders})

@login_required
def download_receipt(request, order_id):
    order = Order.objects.get(pk=order_id)

    try:
        buyer = User.objects.get(pk=order.Buyer_Id)
    except User.DoesNotExist:
        buyer = None

    print("BUYER:", buyer)  # Confirm it’s not None
    # return HttpResponse(f"Buyer: {buyer.first_name} {buyer.last_name} - {buyer.email}")

    try:
        payment = Payment.objects.get(Order_Id=order)
    except Payment.DoesNotExist:
        payment = None

    template_path = 'receipt_template.html'
    context = {
        'order': order,
        'buyer': buyer,
        'payment': payment
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt_{order.Order_Id}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response