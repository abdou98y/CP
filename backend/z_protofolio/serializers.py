from rest_framework import serializers
from .models import *




class CareerPageSerializer(serializers.Serializer):
    head_text=serializers.CharField(max_length=255)
    title=serializers.CharField(max_length=255)
    big_text= serializers.CharField()
    imag= serializers.ImageField()
    
class CareerFormDataSeializer(serializers.Serializer):
    name = serializers.CharField(max_length = 150)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length = 15)
    attachement = serializers.FileField()
    message = serializers.CharField()
    
    def create(self, validated_data):
        return CareerFormData.objects.create(**validated_data)
    
    
    
    
class ContactUsPageSerializer(serializers.Serializer):
    head_text = serializers.CharField(max_length=150)
    title = serializers.CharField(max_length=255)
    location_text = serializers.CharField(max_length=255)
    finish_text = serializers.CharField(max_length=255)
    image = serializers.ImageField()
    
class ContactUsFormDataSeializer(serializers.Serializer):
    name = serializers.CharField(max_length = 150)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length = 15)
    message = serializers.CharField()
    
    def create(self, validated_data):
        return ContactUsFormData.objects.create(**validated_data)
    
