from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Product
from basket.basket import Basket

# Create your views here.
# This function gets all product items in the db
def all_products(request):
    # query all products
    products = Product.products.filter(parent=None).order_by('id').reverse() # filter(parent=None) <- will not display child products || all() <- displays all products

    page = request.GET.get('page', 1)

    # paginated by 6
    # Note: this will only work if you have more than 6 products
    paginator = Paginator(products, 6)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
            products = paginator.page(paginator.num_pages)
    return render(request, 'customerportal/home.html', {'products': products})


# This function gets all the products for each specific product
# Connnected to the category-list.html
def category_list(request):
    categoryList = Category.objects.all().order_by('id')

    return render(request, 'customerportal/products/category-list.html', {'categoryList': categoryList})


# connected to the category-products.html
def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    # filtered data
    categoryProducts = Product.objects.filter(category=category, in_stock=True, parent=None).order_by('id').reverse()

    page = request.GET.get('page', 1)

    # paginated by 6
    # Note: this will only work if you have more than 6 products
    paginator = Paginator(categoryProducts, 6)

    try:
        categoryProducts = paginator.page(page)
    except PageNotAnInteger:
        categoryProducts = paginator.page(1)
    except EmptyPage:
        categoryProducts = paginator.page(paginator.num_pages)

    return render(request, 'customerportal/products/category-products.html', {'category': category, 'categoryProducts': categoryProducts})


# This function gets the details of a specific item product using its slug
def product_detail(request, slug):
    productDetail = get_object_or_404(Product, slug=slug, in_stock=True)
    variants = Product.objects.filter(parent=productDetail, in_stock=True).order_by('id')
    return render(request, 'customerportal/products/detail.html', {'productDetail': productDetail, 'variants': variants}) # 


def clear_product(request):
    user_basket = Basket(request)
    user_basket.clear()
    return reverse("customerportal:all_products")
