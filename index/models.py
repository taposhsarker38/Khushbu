from django.db import models

class Order(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.CharField(max_length=255)
    shipping_name = models.CharField(max_length=255)
    shipping_phone = models.CharField(max_length=15)
    shipping_address = models.TextField()
    shipping_method = models.CharField(max_length=50)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.shipping_name}"
