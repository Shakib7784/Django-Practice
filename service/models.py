from django.db import models

# Create your models here.

class service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField( max_length=50)
    service_des = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)