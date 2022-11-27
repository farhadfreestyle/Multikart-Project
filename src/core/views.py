from django.core.exceptions import ValidationError
from django.shortcuts import render
from core.forms import *
from core.models import Subscribers
from product.models import Product
from django.utils.translation import gettext as _
from product.models import Product, P_Image, Brand
from django.template.defaulttags import register
from django.views.decorators.cache import cache_page
from all_images.models import SliderImages, BrandLogos
from django.views.generic.base import TemplateView
from product.models import Brand


class AboutUs(TemplateView):
    template_name = 'core/about-page.html'

def base(request):
    return render(request, 'base.html')


def error(request):
    return render(request, 'core/404.html')




def contact(request):
    data = {'forms': SendMessageForm}
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise ValidationError
    return render(request, 'core/contact.html', context=data)


def faq(request):
    return render(request, 'core/faq.html')


def index(request):
    
    slider_images = SliderImages.objects.all()

    @register.filter
    def product_images(product, index):
        return P_Image.objects.all().filter(product=product)[index].image.url
    products = Product.objects.all()
    brands = Brand.objects.all()
  

    context = {'products': products, 
    'slider_images': slider_images,
    'brands':brands}

    return render(request, 'core/index.html', context)