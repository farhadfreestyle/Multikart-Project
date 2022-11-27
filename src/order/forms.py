
from django.forms.widgets import TextInput, EmailInput
from django import forms
from order.models  import Checkout
from django.forms import ModelForm
choices = (
    ("1", "India"),
    ("2", "South Africa"),
    ("3", "Australia"),
    ("4", "United States"))
choices2 = (("1", "Free Shipping"), ("2", "Local Pickup"))
choices3 = (("1", "Check Payment"), ("2", "Cash On Delivery"), ("3", "PayPal"))
class Billing(ModelForm):
    first_name = forms.CharField( max_length=30, widget=TextInput(attrs={'required':'true', 'class':'field-label'}))
    last_name = forms.CharField( max_length=30, widget=TextInput(attrs={'required':'true', 'class':'field-label'}))
    phone = forms.CharField( max_length=30, widget=TextInput(attrs={'required':'true', 'class':'field-label'}))
    email = forms.EmailField(label='Email', max_length=50, widget=EmailInput(attrs={'required':'true', 'class':'field-label'}))
    country = forms.ChoiceField(choices=choices)
    address = forms.CharField(max_length=100, widget=TextInput(attrs={'required':'true','placeholder': 'Street address', 'class':'field-label'}))
    town = forms.CharField(max_length=30, widget=TextInput(attrs={'required':'true', 'class':'field-label'}))
    state = forms.CharField(max_length=30, widget=TextInput(attrs={'required':'true', 'class':'field-label'}))
    postal_code = forms.CharField(max_length=30, widget=TextInput(attrs={'required':'true', 'class':'field-label',}))
    shipping = forms.ChoiceField(choices=choices2, widget=forms.RadioSelect(attrs = {'required' : 'true', 'class':'shopping-option'}))
    payment = forms.ChoiceField(choices=choices3, widget=forms.RadioSelect(attrs = {'required' : 'true', 'class':'radio-option'}))
    class Meta:
        model = Checkout
        fields = ['town', 'state', 'postal_code', 'shipping', 'payment',
        ]

    