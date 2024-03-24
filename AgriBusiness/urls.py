
from django.contrib import admin
from django.urls import path
from dashboard import views as d_view
from buyer import  views as b_view
from seller import views as s_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', d_view.home),
    path('product/', d_view.product),
    path('product/<int:product_id>/', d_view.showProduct),
    path('user/', d_view.user),

    path('buyer/', b_view.buyer),
    path('seller/', s_view.seller),

]
