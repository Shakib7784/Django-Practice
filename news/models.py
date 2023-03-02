from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_desc = HTMLField()
    newspaper_name = models.CharField(max_length=50,default="unknown")
    news_img = models.FileField(upload_to="newsimage/",max_length=250,null=True, default=None)

