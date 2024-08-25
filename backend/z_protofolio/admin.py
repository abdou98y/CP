from django.contrib import admin
from django import forms
from PIL import Image
from  io import BytesIO
from django.core.files.base import ContentFile
from django.http import HttpRequest
from .models import *
# Register your models here.


class ImageAdjusterForm(forms.ModelForm):
    class Meta:
        model= CareerPage
        fields=['head_text','title','big_text','imag']
    
    def clean_imag(self):
        image = self.cleaned_data.get('imag')
        if image :
            img = Image.open(image)
            output = BytesIO()
            img.save(output , format='WEBP' , quality=85)
            output.seek(0)
            return ContentFile(output.read(), image.name.split('.')[0] + '.webp')
        return image
        
class CareerPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if CareerPage.objects.exists():
            return False
        return True
    
    form = ImageAdjusterForm

admin.site.register(CareerPage,CareerPageAdmin) 
