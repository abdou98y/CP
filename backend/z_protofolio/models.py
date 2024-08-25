from django.db import models

# Create your models here.
class CareerPage(models.Model):
    head_text = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    big_text = models.TextField()
    imag = models.ImageField(upload_to='z_protofolio/media')
    