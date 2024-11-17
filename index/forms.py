from django import forms

class OrderForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    product_name = forms.CharField(widget=forms.HiddenInput())
    product_price = forms.DecimalField(widget=forms.HiddenInput(), decimal_places=2)
    product_quantity = forms.IntegerField(min_value=1)
    shipping_name = forms.CharField(max_length=255)
    shipping_phone = forms.CharField(max_length=15)
    shipping_address = forms.CharField(max_length=500)
    shipping_method = forms.ChoiceField(choices=[('21', 'ঢাকার ভিতরে - 60TK'), ('22', 'ঢাকার বাইরে - 100TK')])
    shipping_cost = forms.DecimalField(widget=forms.HiddenInput(), decimal_places=2)
    total_amount = forms.DecimalField(widget=forms.HiddenInput(), decimal_places=2)
