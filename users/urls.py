from django.conf.urls import include
from django.urls import path

from .views import dashboard, register, create_profile, update_profile

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/signup', register, name='register'),
    path('accounts/profile/create', create_profile, name='create_profile'),
    path('accounts/profile/update', update_profile, name='update_profile'),
    path('oauth/', include('social_django.urls')),
]