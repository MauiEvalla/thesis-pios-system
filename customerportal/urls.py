# from readline import append_history_file
from django.urls import path
from . import views

app_name = 'customerportal'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('shop/catalogue/', views.category_list, name='category_list'),
    path('shop/<slug:category_slug>', views.category_products, name='category_products'),
    path('<slug:slug>', views.product_detail, name="product_detail"),
    path('clear_product/', views.clear_product, name="clear_product"),
]
