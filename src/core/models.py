from django.db import models

class Subscribers(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    class Meta:
        verbose_name= 'Subscribers'
        verbose_name_plural = verbose_name


class Faq(models.Model):
    questions = models.TextField(max_length=300)
    answers = models.TextField(max_length=300)

    def __str__(self):
        return self.questions
    class Meta:
        verbose_name= 'Faq'
        verbose_name_plural = verbose_name



class Workers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="src/static/workers_image")
    position = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name= 'Workers'
        verbose_name_plural = verbose_name




class SendMessage(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name= 'SendMessage'
        verbose_name_plural = verbose_name

