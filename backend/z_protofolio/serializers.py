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
    








class SingleUpdatPageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    update_name = serializers.CharField(max_length=100)
    discreption = serializers.CharField()
    Image = serializers.ImageField()
    read_more_text = serializers.CharField(max_length=255)
    is_home = serializers.BooleanField()

class AllUpdatesPageserialzer(serializers.Serializer):
    
    title = serializers.CharField(max_length=150)
    updates = SingleUpdatPageSerializer(many = True , read_only =True)
    
class RelatedUpdatesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    update_name = serializers.CharField(max_length=100)
    discreption = serializers.CharField()
    Image = serializers.ImageField()
    
class SingleUpdatePageSerializerWithRelatedUpdatesSerializer(serializers.Serializer):
    body = SingleUpdatPageSerializer()
    relatedupdates=RelatedUpdatesSerializer(many=True,read_only=True)
    
