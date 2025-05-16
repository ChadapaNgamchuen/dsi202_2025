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
    request = models.ForeignKey(DonationRequest, on_delete=models.CASCADE, related_name='offers')
    donater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donation_offers')
    offer_item_description = models.CharField(max_length=255)
    offer_quantity = models.PositiveIntegerField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.donater.username} offers {self.offer_quantity} x {self.offer_item_description} to {self.request.item_name}"