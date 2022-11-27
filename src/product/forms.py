from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea, EmailInput
from product.models import *

class WriteReviewForm(ModelForm):
    name = forms.CharField(max_length=30, widget=TextInput(attrs={'required':'true', 'placeholder': 'Enter Your name', 'class':'form-control', 'id':'name'}),)
    email = forms.CharField(max_length=50,  widget=EmailInput(attrs={'required':'true', 'placeholder': 'Enter Your email', 'class':'form-control', 'id':'email'}))
    review_title = forms.CharField(max_length=1000,widget=TextInput(attrs={'required':'true', 'placeholder': 'Enter Your Review Subjects', 'class':'form-control', 'id':'exampleFormControlTextarea1'}))
    review_desc = forms.CharField(max_length=1000,widget=Textarea(attrs={'required':'true', 'class':'form-control', 'id':'exampleFormControlTextarea1'}))
    

    class Meta:
        model = WriteReview
        fields = ['name','email', 'review_title', "review_desc",]
        
        

class Search(forms.Form):
    input = forms.CharField(max_length=50, widget=TextInput(attrs={'required':'true', 'placeholder': 'Search Products ...', 'class':'form-control', 'aria-label':'Amount (to the nearest dollar)',}),)




class Add_to_Card(forms.Form):
    quantity = forms.IntegerField(widget=TextInput(attrs={'required':'true', 'class':'form-control input-number', 'id':'name', 'name':'quantity', 'value':'1'}))
