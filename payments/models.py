from django.db import models
from bookings.models import Booking

class Payment(models.Model):
    PAYMENT_METHODS = [
        ("mpesa", "M-Pesa"),
        ("card", "Card"),
        ("cash", "Cash"),
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.booking.customer_name}"
