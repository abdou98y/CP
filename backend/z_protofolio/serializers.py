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
    description = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.IntegerField()
    
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

class ProjectCategoriesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class ProjectPageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    project_name = serializers.CharField(max_length=100)
    project_year = serializers.IntegerField()
    svg_logo = serializers.ImageField()
    project_discription = serializers.CharField()
    location_title = serializers.CharField(max_length=100)
    location_text = serializers.CharField(max_length=255)
    category = ProjectCategoriesSerializer()
    main_image = serializers.ImageField()
    overview_title = serializers.CharField(max_length=100)
    overview_text = serializers.CharField()
    poucher_pdf = serializers.FileField()
    poucher_pdf_button = serializers.CharField()
    facility_title = serializers.CharField(max_length=100)
    facility_text = serializers.CharField(max_length=255)
    facities = ProjectFacilitiesInfoSerializer(many =True , read_only=True)
    gallery_text = serializers.CharField(max_length=255)
    gallery_second_text = serializers.CharField()
    gallery_images  =  ProjectGalleryImageSerializer(many =True , read_only =True)
    location_footer_text = serializers.CharField(max_length=100)
    location_description = serializers.CharField()
    map_url = serializers.URLField()
    ifram_map_url = serializers.URLField()
    contact_us_text = serializers.CharField(max_length=255)
    get_direction_button_title =serializers.CharField()
    contact_us_button_title =serializers.CharField()
    
class AllProjectsPageSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)

class AllProjectsPageSingleProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    project_name = serializers.CharField(max_length=100)
    category = ProjectCategoriesSerializer()
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

    def to_representation(self, instance):
        object = AboutUsPage.objects.first()
        
        representation = super().to_representation(instance)
        
        if object and not object.show_founders:
            representation.pop('founder_name', None)
            representation.pop('founder_title', None)
            representation.pop('founder_description', None)
            representation.pop('founder_image', None)
        
        return representation


class AboutUsPageSerializer(serializers.Serializer):
    main_title = serializers.CharField(max_length=100)
    first_title = serializers.CharField(max_length=255)
    second_title = serializers.CharField(max_length=255)
    main_image = serializers.ImageField()
    main_description = serializers.CharField()
    second_section_title = serializers.CharField(max_length=255)
    second_section_description = serializers.CharField()
    company_profile = serializers.FileField()
    download_button_title = serializers.CharField()
    our_mission_title = serializers.CharField(max_length=255)
    our_mission_text = serializers.CharField()
    our_mission_image = serializers.ImageField()
    our_vision_title = serializers.CharField(max_length=255)
    our_vision_text = serializers.CharField()
    our_vision_image = serializers.ImageField()
    mutltible_section_title = serializers.CharField(max_length=100)
    sections = AbouUsSectionSerializer(many=True,read_only=True)
    show_founders = serializers.BooleanField()
    our_founders_title = serializers.CharField(max_length=100)
    founders = AboutUsFounderSerializer(many=True,read_only=True)
    contactus_text = serializers.CharField()
    contactus_button_title = serializers.CharField()
    











class HomePageSliderSerializer(serializers.Serializer):
    slider_image_video = models.FileField()

class HomePageSerializer(serializers.Serializer):
    logo = serializers.ImageField()
    slider_title = serializers.CharField(max_length=255)
    slider_content = HomePageSliderSerializer(many=True,read_only=True)
    about_title = serializers.CharField(max_length=255)
    about_image = serializers.ImageField()
    years_number = serializers.IntegerField()
    years_text = serializers.CharField(max_length=155)
    employee_numbers = serializers.CharField(max_length=50)
    employee_text = serializers.CharField(max_length=155)

class HomePageProjectsSerializer(serializers.Serializer):
    project_name = serializers.CharField(max_length=100)
    project_year = serializers.IntegerField()
    svg_logo = serializers.ImageField()
    project_discription = serializers.CharField()
    gallery_images  =  ProjectGalleryImageSerializer(many =True , read_only =True)
    location_text = serializers.CharField(max_length=255)
    
class HomePageDataSerializer(serializers.Serializer):
    home_page = HomePageSerializer()
    home_page_project = HomePageProjectsSerializer(read_only=True)
    related_projects =AllProjectsPageSingleProjectSerializer(many=True,read_only=True)
    
