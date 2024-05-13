from django.shortcuts import render, get_object_or_404, redirect

from .models import Product,User

def home(request):
    return render(request, 'dashboard.html')

def product(request):
    products = Product.objects.all()

    return render(request, 'products/index.html', {'products': products})
def showProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/show.html', {'product': product})
def createProduct(request):
    return render(request, 'products/create.html')
def saveProduct(request):
    if request.method == 'POST':
        # Extract data from request.POST

        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        # Handle file upload for image
        image = None
        if 'image' in request.FILES:
            image = request.FILES['image']
        
       # Create new instance of Product model
        new_product = Product.objects.create(
            product_name=product_name,
            price=price,
            image=image
        )
        # Redirect to product list page after successful creation
        return render(request, 'products/show.html', {'product': new_product})
        
def updateProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/update.html', {'product': product})
def storeProduct(request):
    if request.method == 'POST':
        # Extract data from request.POST
        id = request.POST.get('id')
        product = get_object_or_404(Product, pk=id)

        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        # Handle file upload for image
        image = None
        if 'image' in request.FILES:
            image = request.FILES['image']
        
        # Update data 
        product.product_name = product_name
        product.price = price
        if image:
            product.image = image
        
        product.save()

        # Redirect to product list page after successful creation
        return render(request, 'products/show.html', {'product': product})
        
def deleteProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('/product/')

def user(request):
    users = User.objects.all()

    return render(request, 'users/index.html', {'users': users})