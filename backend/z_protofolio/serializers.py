from rest_framework import serializers
from .models import *





class CareerPageSerializer(serializers.Serializer):
    head_text=serializers.CharField(max_length=255)
    title=serializers.CharField(max_length=255)
    big_text= serializers.CharField()
    imag= serializers.ImageField()