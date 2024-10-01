from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField( max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(default='Not Provided')
    message = models.TextField()
    
    
# Base User model for common fields
class User(models.Model):
    ROLE_CHOICES = [
        ('seeker', 'Service Seeker'),
        ('provider', 'Service Provider'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)  # Added Register As field

    class Meta:
        abstract = True

# Service Seeker Model
class ServiceSeeker(User):
    # Additional fields specific to Service Seekers can be added here
    def __str__(self):
        return self.name

# Service Provider Model
class ServiceProvider(User):
    SERVICE_TYPE_CHOICES = [
        ('plumbing', 'Plumbing'),
        ('teaching', 'Teaching'),
        ('cleaning', 'Cleaning'),
        ('electrician', 'Electrician'),
    ]
    
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    business_name = models.CharField(max_length=255)
    service_description = models.TextField()
    location = models.CharField(max_length=50)
    home_address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    working_hours = models.CharField(max_length=50)
    shop_image = models.ImageField(upload_to='shop_images/')
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.business_name
