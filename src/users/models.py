
from contextlib import nullcontext
from email.policy import default
from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=30, )
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30 )
    email = models.EmailField(unique=True)
    phone = models.IntegerField(null=True)
    message = models.TextField(null=True)
    flat = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=225, null=True)
    zipcode = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    region = models.CharField(max_length=30, null=True)
    is_active = models.BooleanField(default=True, null=True)
    last_login = models.DateField(null = True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'username']
    


    def __str__(self):
        return self.email  

    def set_username():
        for user in User.objects.all():
            if len(user.username.split())==0:
                user.username = user.email    
                user.save() 
        return
    
    
    
    class Meta:
        verbose_name= 'User'
        verbose_name_plural = 'Users'
        



class Wishlist(models.Model):
    image = models.ImageField(max_length=255)
    product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.image


    class Meta:
        verbose_name= 'Wishlist'
        verbose_name_plural = verbose_name

