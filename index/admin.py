from django.contrib import admin
from .models import  Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'shipping_name','shipping_phone', 'shipping_address','shipping_cost', 'product_price','product_quantity','total_amount','created_at']
