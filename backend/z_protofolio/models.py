from typing import Iterable
from django.db import models
from django.core.files.storage import default_storage
import os
from django.urls import reverse


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



# function  to  make sure only  pdf for poucher
from  django.core.exceptions import ValidationError
def validate_pdf(pdf):
    if not pdf.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')







# function to  make sure that only  maps url is  added
import re
def maps_url(url):
    map_patterns = [
        r'^https://www\.google\.com/maps/',  # Google Maps
        r'^https://maps\.app\.goo\.gl/',      # Google Maps shortened URL
        r'^https://www\.openstreetmap\.org/',# OpenStreetMap
    ]

    if not any(re.match(pattern , url) for pattern in map_patterns):
        raise ValidationError('The URL must be a valid map link (e.g., Google Maps, OpenStreetMap).\n https://www.google.com/maps/ \n https://maps.app.goo.gl/ \n https://www.openstreetmap.org/' )









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






# updates area
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
        
        
        all_updates_page = AllUpdatesPage.objects.first()
        if all_updates_page :
            all_updates_page.updates.add(self)
    def get_update_url(self):
        return reverse('update-detail', args=[self.id])


class AllUpdatesPage(models.Model):
    title = models.CharField(max_length=100)
    updates = models.ManyToManyField(SingleUpdatPage,related_name='updates')
    
    
    
    
    
    
    
    
# projects area
class ProjectGalleryImage(models.Model):
    # project_page = models.ForeignKey(ProjectPage,related_name='gallery_images',on_delete=models.CASCADE,default=1)
    Image = models.ImageField(upload_to='z_protofolio/media/projects')
    
    def save(self ,*args,**kwargs):
        if self.Image:
            self.Image = image_proccesing(self.Image)
        super().save(*args,**kwargs)
        

        
            
class ProjectFacilitiesInfo(models.Model):
    # project_page = models.ForeignKey(ProjectPage, related_name='facities', on_delete=models.CASCADE,default=1)
    facility_info_title = models.CharField(max_length=100)
    facility_info_text = models.CharField(max_length=255)
    facility_info_image = models.ImageField(upload_to='z_protofolio/media/projects')
    
    def save(self,*args,**kwargs):
        if self.facility_info_image:
            self.facility_info_image = image_proccesing(self.facility_info_image)
        super().save(*args,**kwargs)
        


class ProjectPage(models.Model):
    project_name = models.CharField(max_length=100)
    svg_logo = models.ImageField(upload_to='z_protofolio/media/projects')
    project_discription = models.TextField()
    location_title = models.CharField(max_length=100)
    location_text = models.CharField(max_length=255)
    category_title = models.CharField(max_length=100)
    category_text = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='z_protofolio/media/projects')
    overview_title = models.CharField(max_length=100)
    overview_text = models.TextField()
    poucher_pdf = models.FileField(upload_to='z_protofolio/media/poucher',validators=[validate_pdf])
    facility_title = models.CharField(max_length=100)
    facility_text = models.CharField(max_length=255)
    # facities = models.ManyToManyField(ProjectFacilitiesInfo,related_name="facilities_info")
    gallery_title = models.CharField(max_length=100)
    gallery_text = models.CharField(max_length=255)
    # gallery_images = models.ManyToManyField(ProjectGalleryImage,related_name="gallery_images")
    location_footer_text = models.CharField(max_length=100)
    location_description = models.TextField()
    map_url = models.URLField(validators=[maps_url])
    ifram_map_url = models.URLField(validators=[maps_url])
    contact_us_text = models.CharField(max_length=255)
    
    def save(self,*args,**kwargs):
        if self.main_image:
            self.main_image = image_proccesing(self.main_image)
        super().save(*args,**kwargs)
        
class ProjectPageFacilities(models.Model):
    project = models.ForeignKey(ProjectPage, on_delete=models.CASCADE)
    facility = models.ForeignKey(ProjectFacilitiesInfo, on_delete=models.CASCADE)

class ProjectPageGallery(models.Model):
    project = models.ForeignKey(ProjectPage, on_delete=models.CASCADE)
    gallery_image = models.ForeignKey(ProjectGalleryImage, on_delete=models.CASCADE)
                
