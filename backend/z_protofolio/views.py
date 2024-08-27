from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class CareerView(APIView):
    def get(self, request):
        career = CareerPage.objects.get()
        serializer = CareerPageSerializer(career)
        return Response ({"body":serializer.data})


class CareerFormDataPost(APIView):
    def post(self, request):
        serialzer = CareerFormDataSeializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
    








class ContactUSView(APIView):
    def get(self,request):
        contactus = ContactUsPage.objects.get()
        serializer = ContactUsPageSerializer(contactus)
        return Response({"body":serializer.data})

class ContactUsFormDataPost(APIView):
    def post(self ,request):
        serializer = ContactUsFormDataSeializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
    
class AllUpdatesPageView(APIView):
    def get(self,request):
        all_updates = AllUpdatesPage.objects.first()
        serializer = AllUpdatesPageserialzer(all_updates)
        return Response({"body":serializer.data})
    
    
class SingleUpdatePageView(APIView):
    def get(self,request,pk):
        try:
            singleupdate = SingleUpdatPage.objects.get(pk=pk)
        except SingleUpdatPage.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)
        related_updates = SingleUpdatPage.objects.exclude(pk=pk)
        related_serialzer = RelatedUpdatesSerializer(related_updates,many=True)
        serializer = SingleUpdatPageSerializer(singleupdate)
        final_serializer = SingleUpdatePageSerializerWithRelatedUpdatesSerializer({'body': serializer.data,
            'relatedupdates': related_serialzer.data})
        return Response(final_serializer.data)












careerview = CareerView.as_view()
careerformdata = CareerFormDataPost.as_view()
contactusview = ContactUSView.as_view()
contactusformdata = ContactUsFormDataPost.as_view()
updates = AllUpdatesPageView.as_view()
update =  SingleUpdatePageView.as_view()