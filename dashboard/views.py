from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Product,User

def home(request):
    return render(request, 'dashboard.html')

@login_required
def product(request):
    # products = Product.objects.all()
    products = Product.objects.filter(seller_id=request.user)

    return render(request, 'products/index.html', {'products': products})

@login_required
def showProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/show.html', {'product': product})
def createProduct(request):
    return render(request, 'products/create.html')

@login_required
def saveProduct(request):
    if request.method == 'POST':
        # Extract data from request.POST

        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        # Handle file upload for image
        image = None
        if 'image' in request.FILES:
            image = request.FILES['image']
        
       # Create new instance of Product model
        new_product = Product.objects.create(
            product_name=product_name,
            price=price,
            quantity=quantity,
            description=description,
            seller_id=request.user,
            image=image
        )
        # Redirect to product list page after successful creation
        return render(request, 'products/show.html', {'product': new_product})
        
@login_required
def updateProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/update.html', {'product': product})

@login_required
def storeProduct(request):
    if request.method == 'POST':
        # Extract data from request.POST
        id = request.POST.get('id')
        product = get_object_or_404(Product, pk=id)

        product.product_name = request.POST.get('product_name')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.description = request.POST.get('description')
        # Handle file upload for image
        image = None
        if 'image' in request.FILES:
            image = request.FILES['image']
        
        # Update data 
        if image:
            product.image = image
        
        product.save()

        # Redirect to product list page after successful creation
        return render(request, 'products/show.html', {'product': product})

@login_required       
def deleteProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('/product/')

def user(request):
    users = User.objects.all()

    return render(request, 'users/index.html', {'users': users})