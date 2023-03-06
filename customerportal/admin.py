from django.contrib import admin

# Register your models here.
from .models import Category, Product
from safedelete.admin import SafeDeleteAdmin, SafeDeleteAdminFilter, highlight_deleted

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(SafeDeleteAdmin):
    list_display = [highlight_deleted, 'highlight_deleted_field','productName', 'price', 'slug',
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active', SafeDeleteAdminFilter,]
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('productName',)}
    field_to_highlight = 'productName'

