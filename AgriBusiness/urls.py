
from django.contrib import admin
from django.urls import path

from dashboard import views as d_view
from buyer import views as b_view
from seller import views as s_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', d_view.home),
    path('product/', d_view.product),
    path('product/<int:product_id>/', d_view.showProduct),
    path('product/create/', d_view.createProduct),
    path('product/save/', d_view.saveProduct),
    path('product/update/<int:product_id>/', d_view.updateProduct),
    path('product/store/', d_view.storeProduct),
    path('product/delete/<int:product_id>/', d_view.deleteProduct),


    path('user/', d_view.user),


    path('',b_view.home, name ='home'),
    path('signin/',b_view.sign_in, name ='signin.post'),
    path('login/',b_view.sign_in, name ='login'),
    path('logout/',b_view.logout, name ='logout'),
    path('signup/',b_view.sign_up, name ='signup'),
    path('buyer/',b_view.buyer, name ='buyer'),
    path('inventory/',b_view.inventory, name ='inventory'),


    path('add_Buyer/', b_view.add_Buyer, name = 'add_buyer'),
    path('add_Seller/', b_view.add_Seller, name = 'add_seller'),


    path('market/',b_view.market, name ='market'),
    path('market/product-details/<int:product_id>',b_view.productDetails, name ='productDetails'),
    path('cart/add', b_view.addToCart, name = 'add_to_cart'),
    path('cart', b_view.showCart),
    path('cart/remove/<int:item_id>/', b_view.remove_from_cart, name='remove_from_cart'),

    path('checkout/', b_view.checkout),
    path('checkout/make', b_view.checkoutMake),
    path('order', b_view.showOrders),


    path('seller/',s_view.seller, name ='seller'),


]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
