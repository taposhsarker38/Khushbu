
from .models import Order  # Replace with your model if necessary
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render,redirect
import re
def checkout(request):
    if request.method == 'POST':
        # Retrieve form data
        shipping_name = request.POST.get('shipping_name')
        shipping_phone = request.POST.get('shipping_phone')
        shipping_method = request.POST.get('shipping_method')
        shipping_address = request.POST.get('shipping_address')
        product_id = request.POST.get('product_id')
        product_quantity = request.POST.get('product_quantity')
        product_price = request.POST.get('product_price')
        shipping_cost = request.POST.get('shipping_cost')
        total_amount = request.POST.get('total_amount')
        product_name = request.POST.get('product_name')
        
        # Validate product ID
        if not product_id or not product_id.isdigit():
            return JsonResponse({'success': False, 'msg': 'Invalid product ID.'})

        # Validate product quantity
        try:
            product_quantity = int(product_quantity)
            if product_quantity < 1:
                return JsonResponse({'success': False, 'msg': 'Quantity must be at least 1.'})
        except (ValueError, TypeError):
            return JsonResponse({'success': False, 'msg': 'Invalid quantity.'})

        # Validate product price
        try:
            product_price = float(product_price)
            if product_price <= 0:
                return JsonResponse({'success': False, 'msg': 'Price must be greater than 0.'})
        except (ValueError, TypeError):
            return JsonResponse({'success': False, 'msg': 'Invalid price.'})

        # Validate shipping cost
        try:
            shipping_cost = float(shipping_cost)
            if shipping_cost < 0:
                return JsonResponse({'success': False, 'msg': 'Shipping cost cannot be negative.'})
        except (ValueError, TypeError):
            return JsonResponse({'success': False, 'msg': 'Invalid shipping cost.'})

        # Validate total amount
        try:
            total_amount = float(total_amount)
            if total_amount <= 0:
                return JsonResponse({'success': False, 'msg': 'Total amount must be greater than 0.'})
        except (ValueError, TypeError):
            return JsonResponse({'success': False, 'msg': 'Invalid total amount.'})

        # If all validations pass, save the order
        # Replace 'Order' with your model name if different
        order = Order.objects.create(
            shipping_name=shipping_name,
            shipping_phone=shipping_phone,
            shipping_method=shipping_method,
            shipping_address=shipping_address,
            product_id=product_id,
            product_quantity=product_quantity,
            product_price=product_price,
            shipping_cost=shipping_cost,
            total_amount=total_amount,
            product_name=product_name,
        )
        order.save()

        return redirect('order_success')

    return render(request, 'index.html')
def order_success(request):
    # Get the message from the query parameter, if available
    message = request.GET.get('msg', 'Thank you for your order!')
    return render(request, 'success.html', {'message': message})
