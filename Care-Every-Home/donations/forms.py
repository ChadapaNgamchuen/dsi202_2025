# donations/forms.py
from django import forms
from .models import DonationRequest,DonationOffer

class DonationRequestForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        fields = ['item_name', 'quantity', 'reason']
# ถ้าอยาก debug จริงๆ ให้ทำข้างนอก
print("✅ DonationRequestForm loaded with fields:", DonationRequestForm._meta.fields)

class DonationOfferForm(forms.ModelForm):
    class Meta:
        model = DonationOffer
        fields = ['offer_item_description', 'offer_quantity', 'message']
