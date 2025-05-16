from django.contrib import admin
from .models import DonationRequest, Donation, DonationOffer

admin.site.register(Donation)
admin.site.register(DonationRequest)
admin.site.register(DonationOffer)