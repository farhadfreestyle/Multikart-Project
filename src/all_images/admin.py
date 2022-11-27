from django.contrib import admin

# Register your models here.

from .models import BrandLogos, SliderImages


admin.site.register(BrandLogos)
admin.site.register(SliderImages)