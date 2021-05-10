from django.urls import path
from .  import views as uv

urlpatterns = [
    path('', uv.home, name='homepage'),
    path('about/', uv.about, name='about'),
    path('services/', uv.services, name='services'),
    path('contact/', uv.contact, name='contact'),
    path('profile/', uv.profile, name='profile'),
   
]