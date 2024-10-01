from django.contrib import admin
from .models import *
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','email','message']

admin.site.register(Contact)

@admin.register(ServiceSeeker)
class ServiceSeekerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'service_type', 'location')