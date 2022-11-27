from django.db import models


class SliderImages(models.Model):
    slider_image = models.ImageField(upload_to="src/static/index-images")
    gender = models.BooleanField(default=False, null=True)
    text = models.TextField(null=True)

    class Meta:
        verbose_name = 'SliderImage'
        verbose_name_plural = 'SliderImages'


class BrandLogos(models.Model):
    logos = models.ImageField()

    class Meta:
        verbose_name = 'BrandLogo'
        verbose_name_plural = 'BrandLogos'