from django.db import models


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=50, default="Example Work")
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()
    web_address = models.URLField(max_length=200)