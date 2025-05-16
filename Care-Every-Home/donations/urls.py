from django.urls import path
from .views import home, browse_requests, donation_offer, my_requests,create_donation_request




urlpatterns = [
    path('', home, name='donation_home'),
    path('requests/', browse_requests, name='browse_requests'),  
    path('my-requests/',my_requests, name='my_requests'), 
    path('requests/<int:request_id>/offer/', donation_offer, name='donation_offer'),
    path('requests/create/', create_donation_request, name='create_request'),

]
