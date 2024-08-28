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
    
class AllUpdatesPageSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    
class AllUpdatesDataserialzer(serializers.Serializer):
    title = AllUpdatesPageSerializer()
    updates = SingleUpdatPageSerializer(many = True , read_only =True)
    
class RelatedUpdatesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    update_name = serializers.CharField(max_length=100)
    discreption = serializers.CharField()
    Image = serializers.ImageField()
    
class SingleUpdatePageSerializerWithRelatedUpdatesSerializer(serializers.Serializer):
    body = SingleUpdatPageSerializer()
    relatedupdates=RelatedUpdatesSerializer(many=True,read_only=True)
    







class ProjectGalleryImageSerializer(serializers.Serializer):
    Image = serializers.ImageField()
    
class ProjectFacilitiesInfoSerializer(serializers.Serializer):
    facility_info_title = serializers.CharField(max_length=100)
    facility_info_text = serializers.CharField(max_length=255)
    facility_info_image = serializers.ImageField()

class ProjectPageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    project_name = serializers.CharField(max_length=100)
    project_year = serializers.IntegerField()
    svg_logo = serializers.ImageField()
    project_discription = serializers.CharField()
    location_title = serializers.CharField(max_length=100)
    location_text = serializers.CharField(max_length=255)
    category_title = serializers.CharField(max_length=100)
    category_text = serializers.CharField(max_length=255)
    main_image = serializers.ImageField()
    overview_title = serializers.CharField(max_length=100)
    overview_text = serializers.CharField()
    poucher_pdf = serializers.FileField()
    facility_title = serializers.CharField(max_length=100)
    facility_text = serializers.CharField(max_length=255)
    facities = ProjectFacilitiesInfoSerializer(many =True , read_only=True)
    gallery_text = serializers.CharField(max_length=255)
    gallery_images  =  ProjectGalleryImageSerializer(many =True , read_only =True)
    location_footer_text = serializers.CharField(max_length=100)
    location_description = serializers.CharField()
    map_url = serializers.URLField()
    ifram_map_url = serializers.URLField()
    contact_us_text = serializers.CharField(max_length=255)
    
    
class AllProjectsPageSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)

class AllProjectsPageSingleProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    project_name = serializers.CharField(max_length=100)
    project_year = serializers.IntegerField()
    main_image = serializers.ImageField()
    
class AllProjectsDataSerializer(serializers.Serializer):
    title = AllProjectsPageSerializer()
    data = AllProjectsPageSingleProjectSerializer(many=True,read_only=True)










class AbouUsSectionSerializer(serializers.Serializer):
    section_title = serializers.CharField(max_length=100)
    section_text = serializers.CharField(max_length=255)
    section_description = serializers.CharField()
    section_image = serializers.ImageField()


class AboutUsFounderSerializer(serializers.Serializer):
    founder_name = serializers.CharField(max_length=100)
    founder_title = serializers.CharField(max_length=100)
    founder_description = serializers.CharField()
    founder_image = serializers.ImageField()


class AboutUsPageSerializer(serializers.Serializer):
    main_title = serializers.CharField(max_length=100)
    first_title = serializers.CharField(max_length=255)
    second_title = serializers.CharField(max_length=255)
    main_image = serializers.ImageField()
    main_description = serializers.CharField()
    second_section_title = serializers.CharField(max_length=255)
    second_section_description = serializers.CharField()
    company_profile = serializers.FileField()
    our_mission_title = serializers.CharField(max_length=255)
    our_mission_text = serializers.CharField()
    our_mission_image = serializers.ImageField()
    our_vision_title = serializers.CharField(max_length=255)
    our_vision_text = serializers.CharField()
    our_vision_image = serializers.ImageField()
    mutltible_section_title = serializers.CharField(max_length=100)
    sections = AbouUsSectionSerializer(many=True,read_only=True)
    our_founders_title = serializers.CharField(max_length=100)
    founders = AboutUsFounderSerializer(many=True,read_only=True)
    contactus_text = serializers.CharField()
    
