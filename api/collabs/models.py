from django.db import models
from api.user.models import CustomUser
# Create your models here.

class Collaboration(models.Model):
    business = models.ForeignKey(CustomUser, related_name="business_collabs", on_delete=models.CASCADE, limit_choices_to={'role': 'business'})
    influencer = models.ForeignKey(CustomUser, related_name="influencer_collabs", on_delete=models.CASCADE, limit_choices_to={'role': 'influencer'})
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ), default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    reviewed = models.BooleanField(default=False)
    review_positive = models.BooleanField(null=True)  


    def __str__(self):
        return f"{self.business.name} → {self.influencer.name} ({self.status})"
    
    