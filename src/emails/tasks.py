from __future__ import absolute_import, unicode_literals
import celery
from celery import shared_task
from django.core.mail import send_mail
from product.models import Product, WriteReview
from users.models import User
from datetime import datetime
from django.template.loader import render_to_string 
from django.utils.html import strip_tags
from django.conf import settings
from .services import products_to_send
from django_celery_beat.models import PeriodicTask






@shared_task(bind = True)
def monthly_email_sender(self):
    
    
    subject = 'We have new products!!!'
    message = render_to_string('emails/new_products.txt')

    context = {
        
        }
    html_content = render_to_string('emails/new_products.html', context=context)
    message = render_to_string('emails/new_products.txt')

    context = {
        'products':products_to_send.products_to_send

        }
    html_content = render_to_string('emails/new_products.html', context=context)
                

    send_mail(subject = subject, 
            message=message,
            html_message=html_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['farhad.aghayev7077@gmail.com'])




