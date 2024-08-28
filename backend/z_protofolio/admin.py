from django.contrib import admin
from django import forms
from django.http import HttpRequest
from .models import *




# career page area
#adjustin the  career page default admin behvior & 
class CareerPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if CareerPage.objects.exists():
            return False
        return True

class CareerFormDataAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','attachement','message']
    readonly_fields = ['name','email','phone','attachement','message']
    
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request,obj=None):
        return False
    def has_delete_permission(self, request,obj=None):
        return False
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset






# conatct us page area
#adjustin the  career page default admin behvior
class ContactUsPageAdmin(admin.ModelAdmin): 
    def has_add_permission(self, request):
        if ContactUsPage.objects.exists():
            return False
        return True

class ContactUsFormDataAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','message']
    readonly_fields = ['name','email','phone','message']
    
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request,obj=None):
        return False
    def has_delete_permission(self, request,obj=None):
        return False
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset




# allupdates page area
#adjustin the  allupdates page default admin behvior
class AllUpdatesPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AllUpdatesPage.objects.exists():
            return False
        return True





# all projects  page area
class AllProjectsPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AllProjectsPage.objects.exists():
            return False
        return True






# about us page area 
class AboutUsPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AboutUsPage.objects.exists():
            return False
        return True







admin.site.register(CareerPage,CareerPageAdmin) 
admin.site.register(CareerFormData,CareerFormDataAdmin)
admin.site.register(ContactUsPage,ContactUsPageAdmin)
admin.site.register(ContactUsFormData,ContactUsFormDataAdmin)
admin.site.register(SingleUpdatPage)
admin.site.register(AllUpdatesPage,AllUpdatesPageAdmin)
admin.site.register(ProjectPage)
admin.site.register(ProjectFacilitiesInfo)
admin.site.register(ProjectGalleryImage)
admin.site.register(AllProjectsPage,AllProjectsPageAdmin)
admin.site.register(AboutUsPage,AboutUsPageAdmin)
admin.site.register(AboutUsSection)
admin.site.register(AboutUsFounder)

