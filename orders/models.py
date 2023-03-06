from decimal import Decimal
from django.conf import settings
from django.db import models
import uuid

from customerportal.models import Product


class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    table_number = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_bill = models.DecimalField(max_digits=5, decimal_places=2)
    complete = models.BooleanField(default=False)

    ORDER_STATUS = [
        ('preparing', 'PREPARING'),
        ('serving', 'SERVING'),
        ('order completed', 'ORDER_COMPLETED'),
    ]
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS, default='preparing')

    class Meta:
        ordering = ('-created',)

    #shows what is first thing you will see in the database
    def __str__(self):
        return F"Transaction ID: {str(self.id)}"

# everypurchase will be rendered here
class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Ordered Item'

    def __str__(self):
        return f"Order ID: {self.order}"

