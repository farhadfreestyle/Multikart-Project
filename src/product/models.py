from time import timezone
from datetime import datetime
from unicodedata import category
from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.utils.text import slugify
from django.urls import reverse
import string
import random


class Product(models.Model):
    name = models.CharField(max_length=30, default='name')
    price = models.FloatField(null=True)
    discount_percent = models.IntegerField(null=False, default=55)
    title = models.CharField(max_length=50, null=True)
    availablity = models.BooleanField(null=True)
    rating = models.FloatField(default=0)
    status = models.BooleanField(default=False)
    color = models.ManyToManyField('product.color', )
    category = models.ManyToManyField('product.category', )
    size = models.ManyToManyField('product.size')
    brand = models.ManyToManyField('product.brand')
    description = models.TextField(default='This is the desciption of this item')
    fabric = models.CharField(max_length=30, default='silk')
    material = models.CharField(max_length=30, null=True)
    video = models.FileField(null=True, upload_to="src/static/product_videos")
    quantity = models.IntegerField(default=0)
    created_at = models.DateField(default=datetime.now)
    digital = models.BooleanField(default=False, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def colors(self):
        return "\n".join([p.color for p in self.color.all()])

    def categories(self):
        return "\n".join([p.category for p in self.category.all()])

    def brands(self):
        return "\n".join([p.brand for p in self.brand.all()])

    def sizes(self):
        return "\n".join([p.size for p in self.size.all()])

    def get_images(self):
        return self.image_set.all().order_by("id")

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Product)


#####################################################################


class Brand(models.Model):
    brand = models.CharField(max_length=30)
    brand_logo =  models.ImageField(upload_to="src/static/brand_logos", null=True)

    def __str__(self):
        return self.brand


#####################################################################
class WriteReview(models.Model):
    name = models.CharField(max_length=30)
    rating = models.IntegerField(null=True)
    email = models.EmailField()
    review_title = models.CharField(max_length=50)
    review_desc = models.TextField(max_length=300)
    product = models.ForeignKey('product.product', on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'WriteReview'


#####################################################################


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        verbose_name_plural = verbose_name

    #####################################################################


class P_Image(models.Model):
    image_name = models.CharField(max_length=30, default='image')
    image = models.ImageField(upload_to="src/static/product_images")
    product = models.ForeignKey('product.product', on_delete=models.CASCADE, related_name="image_set", default=None)

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name = 'P_Image'
        verbose_name_plural = 'P_Images'

    #####################################################################


class Color(models.Model):
    color = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    #####################################################################


class Size(models.Model):
    size = models.CharField(max_length=30, default='L', unique=True)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    #####################################################################


class Sale(models.Model):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, default=None)
    amount = models.FloatField()
    enddate = models.DateField()

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Sales'
        verbose_name_plural = 'Sales'