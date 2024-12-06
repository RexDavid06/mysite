from django.urls import path
from .views import *

urlpatterns = [
    path('', home , name='home'),
    path('about/', about , name='about'),
    path('resume/', resume , name='resume'),
    path('services/', services , name='services'),
    path('portfolio/', portfolio , name='portfolio'),
    path('contact/', contact , name='contact'),
    path('service-details/', service_details , name='service-details'),
    path('download-resume/', download_resume, name='download_resume'),
]