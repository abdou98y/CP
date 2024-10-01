from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class CareerView(APIView):
    def get(self, request):
        career = CareerPage.objects.get()
        serializer = CareerPageSerializer(career,context={'request': request})
        return Response ({"body":serializer.data})
    
    def post(self, request):
        serialzer = CareerFormDataSeializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


    
    








class ContactUSView(APIView):
    def get(self,request):
        contactus = ContactUsPage.objects.get()
        serializer = ContactUsPageSerializer(contactus,context={'request': request})
        return Response({"body":serializer.data})

    def post(self ,request):
        serializer = ContactUsFormDataSeializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    
    
    
    
    
    
    
class AllUpdatesPageView(APIView):
    def get(self,request):
        all_updates_title = AllUpdatesPage.objects.first()
        all_updates_data= SingleUpdatPage.objects.all()
        all_updates = SingleUpdatPageSerializer(all_updates_data,many=True)
        title = AllUpdatesPageSerializer(all_updates_title)
        body = AllUpdatesDataserialzer({'title':title.data,'updates':all_updates.data},context={'request': request})
        return Response({"body":body.data})
    
    
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
            'relatedupdates': related_serialzer.data},context={'request': request})
        return Response(final_serializer.data)





class ProjectPageView(APIView):
    def get(self,request,pk):
        projectpage = ProjectPage.objects.get(pk = pk)
        serializer = ProjectPageSerializer(projectpage,context={'request': request})
        return Response({'body':serializer.data})

class AllProjectsView(APIView):
    def get(self,request):
        allprojectstitle = AllProjectsPage.objects.first()
        title_serializer = AllProjectsPageSerializer(allprojectstitle)
        allprojectdata = ProjectPage.objects.all()
        data_serializer = AllProjectsPageSingleProjectSerializer(allprojectdata,many=True)
        fullpage = AllProjectsDataSerializer({'title':title_serializer.data,'data':data_serializer.data},context={'request': request})
        return Response({'body':fullpage.data})


class AboutUsPageView(APIView):
    def get(self,request):
        aboutus = AboutUsPage.objects.first()
        aboutus_serialized = AboutUsPageSerializer(aboutus,context={'request': request})
        return Response({"body":aboutus_serialized.data})




class HomePageView(APIView):
    def get(self,request):
        homepage = HomePage.objects.first()
        serialzed_homepage = HomePageSerializer(homepage)
        homeproject=ProjectPage.objects.get(is_home=True)
        serialzed_homeproject = HomePageProjectsSerializer(homeproject)
        relatedprojects= ProjectPage.objects.exclude(is_home=True)[0:2]
        serialzed_relatedprojects=AllProjectsPageSingleProjectSerializer(relatedprojects,many=True)
        homepagedata = HomePageDataSerializer({'home_page':serialzed_homepage.data,'home_page_project':serialzed_homeproject.data,'related_projects':serialzed_relatedprojects.data},context={'request': request})
        return Response({'body':homepagedata.data})



class FooterView(APIView):
    def get(self,request):
        footer = Footer.objects.first()
        serialized_footer = FooterSerializer(footer)
        return Response({'footer':serialized_footer.data})

careerview = CareerView.as_view()
contactusview = ContactUSView.as_view()
updates = AllUpdatesPageView.as_view()
update =  SingleUpdatePageView.as_view()
projectpage = ProjectPageView.as_view()
projects = AllProjectsView.as_view()
aboutus =  AboutUsPageView.as_view()
home = HomePageView.as_view()
footer = FooterView.as_view()