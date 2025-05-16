from django.urls import path
from .views import home, browse_requests

urlpatterns = [
    path('', home, name='donation_home'),
    path('requests/', browse_requests, name='browse_requests'),   
]
