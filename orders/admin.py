from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
  list_display = ['id', 'table_number', 'created', 'order_status', 'total_bill']

class OrderItemAdmin(admin.ModelAdmin):
  list_display = ['order', 'product', 'quantity']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
