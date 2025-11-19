from django.db import models
from django.contrib.auth.models import User  # <-- add this

class Property(models.Model):
    PROPERTY_TYPES = [
        ('SALE', 'For Sale'),
        ('RENT', 'For Rent'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    area_sqft = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)
    agent = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.location}"
