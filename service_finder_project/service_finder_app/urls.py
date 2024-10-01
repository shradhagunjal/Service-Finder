from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('contact_form',contact_form,name = "contact_form"),
    path('register_form',register_form,name = "register_form"),
    path('services_providers/', service_providers_view, name='service_providers'),
]