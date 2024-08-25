from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class CareerView(APIView):
    def get(self, request):
        career = CareerPage.objects.get()
        serializer = CareerPageSerializer(career)
        return Response ({"body":serializer.data})

my_view = CareerView.as_view()