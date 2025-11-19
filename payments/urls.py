from django.urls import path
from . import views

urlpatterns = [
    path('<int:booking_id>/pay/', views.payment_create, name='payment_create'),
    path('success/<int:payment_id>/', views.payment_success, name='payment_success'),
]
