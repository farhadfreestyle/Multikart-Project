from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea, EmailInput
from core.models import *

class SendMessageForm(ModelForm):
    first_name = forms.CharField(max_length=30, widget=TextInput(attrs={'required':'true', 'placeholder': 'Enter Your first name', 'class':'form-control', 'id':'name'}),)
    last_name = forms.CharField(max_length=30,  widget=TextInput(attrs={'required':'true', 'placeholder': 'Enter Your last name', 'class':'form-control', 'id':'last-name'}))
    email = forms.CharField(max_length=50,  widget=EmailInput(attrs={'required':'true', 'placeholder': 'Enter Your email', 'class':'form-control', 'id':'email'}))
    phone_number = forms.CharField(max_length=50, widget=TextInput(attrs={'required':'true', 'placeholder': 'Enter Your phone number', 'class':'form-control', 'id':'review'}))
    message = forms.CharField(max_length=1000,widget=Textarea(attrs={'required':'true', 'placeholder': 'Enter Your message', 'class':'form-control', 'id':'exampleFormControlTextarea1'}))
    class Meta:
        model = SendMessage
        fields = ['first_name', 'last_name','phone_number' ,'email', 'message']
        
        
class Subscribe(ModelForm):
     email = forms.CharField(max_length=50,  widget=EmailInput(attrs={'required':'true', 'placeholder': 'Enter Your email', 'class':'form-control', 'id':'email', 'onfocus':"this.value=''"}))
     class Meta:
        model = Subscribers
        fields = ['email']

