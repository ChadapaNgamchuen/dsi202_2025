from django.db import models
from django.contrib.auth.models import User

class DonationRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations_requests')
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.item_name} x{self.quantity} by {self.requester.username}"

class DonationOffer(models.Model):
    donater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations_offers')
    message = models.TextField(blank=True)
    offer_item_description = models.CharField(max_length=255)  # อธิบายสิ่งที่จะบริจาค
    offer_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)  # ถ้า requester กดตอบรับ ก็ค่อย mark true

    def __str__(self):
        return f"{self.donater.username} offers to {self.request.item_name}"


