from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as users_views  

urlpatterns = [
    path('', users_views.home, name='home'),  
    path('login/', users_views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('admin/', admin.site.urls),
    path('properties/', include('properties.urls')),
    path('bookings/', include('bookings.urls')),
    path('payments/', include('payments.urls')),
    path('signup/', users_views.signup, name='signup'),
]
