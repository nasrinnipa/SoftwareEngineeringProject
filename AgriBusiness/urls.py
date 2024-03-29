
from django.contrib import admin
from django.urls import path
from dashboard import views as d_view
from buyer import  views as b_view
from seller import views as s_view
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', d_view.home),
    path('product/', d_view.product),
    path('product/<int:product_id>/', d_view.showProduct),
    path('user/', d_view.user),


    path('',b_view.home, name ='home'),
    path('signin/',b_view.sign_in, name ='Sign In'),
    path('signup/',b_view.sign_up, name ='Sign Up'),
    path('seller/',b_view.seller, name ='seller'),
    path('buyer/',b_view.buyer, name ='buyer'),
    path('inventory/',b_view.inventory, name ='inventory'),
]
