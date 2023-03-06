from email.policy import default
from enum import unique
from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE
from safedelete.models import SOFT_DELETE
from safedelete.managers import SafeDeleteManager
from safedelete.managers import DELETED_VISIBLE
from ckeditor.fields import RichTextField


# Create your models here.
class ProductManager(SafeDeleteManager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(SafeDeleteModel):
    deleted_by_cascade = None
    _safedelete_policy = SOFT_DELETE
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/', default="images/default.jpeg")

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("customerportal:category_products", args=[self.slug])

    def __str__(self):
        return self.name


class Product(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    parent = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    productName = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = RichTextField(blank=True, max_length=255)
    image = models.ImageField(upload_to='images/', default="images/default.jpeg")
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    sellers_note = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()


    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)
        

    def get_absolute_url(self):
        return reverse("customerportal:product_detail", args=[self.slug])

    def __str__(self):
        return self.productName

