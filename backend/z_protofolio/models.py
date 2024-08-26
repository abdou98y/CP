from typing import Iterable
from django.db import models
from django.core.files.storage import default_storage
import os



# function  to  convert  images to  webp 
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image
def image_proccesing(image):
    if image:
        img = Image.open(image)
        output = BytesIO()
        img.save(output, format='WEBP', quality=85)
        output.seek(0)
        return ContentFile(output.read(), image.name.split('.')[0] + '.webp')
    return image










# Career page
class CareerPage(models.Model):
    head_text = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    big_text = models.TextField()
    imag = models.ImageField(upload_to='z_protofolio/media/career')
    
    def save(self, *args, **kwargs):
        if self.imag:
            self.imag = image_proccesing(self.imag)
        super().save(*args, **kwargs)
        
class CareerFormData(models.Model):
    name = models.CharField(max_length=150)
    email  = models.EmailField()
    phone = models.CharField(max_length=15)
    attachement = models.FileField(upload_to='uploads/')
    message = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.id}_{self.name}"
    
    def save(self ,*args, **kwargs):
        super().save(*args,**kwargs)
        
        if self.attachement :
            folder_path =  os.path.join('uploads',str(self.id)+'_'+self.name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            old_file_path = self.attachement.path
            new_file_path =  os.path.join(folder_path,os.path.basename(old_file_path))
            default_storage.save(new_file_path,self.attachement)
            self.attachement.name = os.path.join(folder_path, os.path.basename(old_file_path))
            super().save(update_fields=['attachement'])











#contactus  page
class ContactUsPage(models.Model):
    head_text = models.CharField(max_length=150)
    title = models.CharField(max_length=255)
    location_text = models.CharField(max_length=255)
    finish_text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='z_protofolio/media/contactus')
    
    def save(self, *args, **kwargs):
        if self.image:
            self.image = image_proccesing(self.image)
        super().save(*args, **kwargs)

class ContactUsFormData(models.Model):
    name = models.CharField(max_length=150)
    email  = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.id}_{self.name}"


class SingleUpdatPage(models.Model):
    update_name = models.CharField(max_length=100)
    discreption = models.TextField()
    Image = models.ImageField(upload_to='z_protofolio/media/updates')
    read_more_text = models.CharField(max_length=255)
    is_home = models.BooleanField()
    
    def save(self,*args,**kwargs):
        if self.Image:
            self.Image = image_proccesing(self.Image)
        super().save(*args,**kwargs)

class AllUpdatesPage(models.Model):
    title = models.CharField(max_length=100)
    updates = models.ManyToManyField(SingleUpdatPage,name='updates')
    