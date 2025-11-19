from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('<int:id>/edit/', views.booking_edit, name='booking_edit'),
    path('create/<int:property_id>/', views.booking_create, name='booking_create'),
]
