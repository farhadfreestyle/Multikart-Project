from django import forms
from django.forms.widgets import TextInput, Textarea, EmailInput, PasswordInput
from users.models import *
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import ModelForm
from django.contrib.auth import get_user_model





User = get_user_model()

class RegsiterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=TextInput(attrs={'required':'true', 'placeholder': 'Enter Your name', 'class':'form-control', 'id':'name'}),)
    last_name = forms.CharField(max_length=30, widget=TextInput(attrs={'required':'true', 'placeholder': 'Enter Your name', 'class':'form-control', 'id':'name'}),)
    email = forms.CharField(max_length=50,  widget=EmailInput(attrs={'required':'true', 'placeholder': 'Enter Your email', 'class':'form-control', 'id':'email'}))
    password1 = forms.CharField(min_length=5, max_length=30, widget=PasswordInput(attrs={'required':'true', 'placeholder':'Enter your password', 'class':'form-control', 'id':'review'}))
    password2 = forms.CharField(min_length=5, max_length=30, widget=PasswordInput(attrs={'required':'true', 'placeholder':'Enter your password again', 'class':'form-control', 'id':'review'}))
    

    
    
    class Meta:
        model = User
        fields = ("first_name", 'last_name', 'email','password1', 'password2')


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50,  widget=EmailInput(attrs={'required':'true', 'placeholder': 'Enter Your email', 'class':'form-control', 'id':'email'}))
    password = forms.CharField(min_length=5, max_length=30, widget=PasswordInput(attrs={'required':'true', 'placeholder':'Enter your password', 'class':'form-control', 'id':'review'}))








        
        
       
        
        
