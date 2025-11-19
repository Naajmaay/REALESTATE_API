from django.db import models
from properties.models import Property
from django.contrib.auth.models import User  # <-- added

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    buyer_name = models.CharField(max_length=100)
    email = models.EmailField()
    booking_date = models.DateField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.buyer_name} - {self.property.title}"
