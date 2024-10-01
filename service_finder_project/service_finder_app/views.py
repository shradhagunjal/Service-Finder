from django.http import JsonResponse
from django.shortcuts import redirect, render
import requests
from .models import *
from django_ratelimit.core import is_ratelimited
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def contact_form(request):
    
    if request.method == "POST":
        rate_limited = is_ratelimited(request, key='ip', rate='2/5m', method=['POST'], increment=True,group='contact_form')

        if rate_limited:
            return JsonResponse({'message': 'Message already send. Try again later.'}, status=429)
        
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': '6LfPeEgqAAAAAM-NieldmNacoP0Du7fIHIvau289',  
            'response': recaptcha_response
        }
        
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        
        if not result.get('success'):
            return JsonResponse({'message': 'Invalid reCAPTCHA, failed.'}, status=400)
        
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact = Contact(name= name,mobile = mobile,email = email, message = message)
        
        contact.save()
        return JsonResponse({'message': 'Success'}, status=200)

    return JsonResponse({'message': 'Invalid request'}, status=400)


def register_form(request):
    if request.method == "POST":
        user_type = request.POST.get('user_type')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if ServiceSeeker.objects.filter(email=email).exists():
            return JsonResponse({'email': ['Email is already registered.']}, status=409)
        
        if ServiceProvider.objects.filter(email=email).exists():
            return JsonResponse({'email': ['Email is already registered.']}, status=409)
        
        if user_type == 'provider':
            service_type = request.POST.get('service_type')
            business_name = request.POST.get('business_name')
            service_description = request.POST.get('service_description')
            location = request.POST.get('location')
            home_address = request.POST.get('home_address')
            contact_number = request.POST.get('contact_number')
            working_hours = request.POST.get('working_hours')
            shop_image = request.FILES.get('shop_image')
            website = request.POST.get('website')
            
            shop_image = request.FILES.get('shop_image')

            # Create Service Provider instance
            provider = ServiceProvider(
                name=name,
                email=email,
                password=password,  # Hash the password
                role='provider',
                service_type=service_type,
                business_name=business_name,
                service_description=service_description,
                location=location,
                home_address=home_address,
                contact_number=contact_number,
                working_hours=working_hours,
                shop_image=shop_image,
                website=website,
            )
            
            if shop_image:
                provider.shop_image = shop_image
                
            provider.save()
            return JsonResponse({'message': 'Success'}, status=200)

        if user_type == 'seeker':
            # Create Service Seeker instance
            seeker = ServiceSeeker(
                name=name,
                email=email,
                password=password,  
                role='seeker'
            )
            seeker.save()
            return JsonResponse({'message': 'Success'}, status=200)
        
        return JsonResponse({'message': 'Invalid request'}, status=400)

    return JsonResponse({'message': 'Invalid request'}, status=400)

def service_providers_view(request):
    query = request.GET.get('q', None)  # Get the search query from the URL parameters
    service_providers = ServiceProvider.objects.all()

    if query:
        # Filter service providers based on the search query
        service_providers = service_providers.filter(
            service_type=query
        )

    context = {
        'service_providers': service_providers
    }
    return render(request, 'service.html', context)

