from django.urls import path
from .views import custom_login, signup, home, logout_view

urlpatterns = [
    path('login/', custom_login, name='login'),
    path('signup/', signup, name='signup'),
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
]
