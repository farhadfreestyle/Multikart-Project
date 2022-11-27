from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from tasks import monthly_email_sender


def send_email():
    monthly_email_sender.delay()
    

        
        



