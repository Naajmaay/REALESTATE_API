from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('<int:id>/', views.property_detail, name='property_detail'),
    path('<int:id>/edit/', views.property_edit, name='property_edit'),
]
