# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, default='Anonymous', null=True, blank=True)
    email = models.EmailField(unique=True, max_length=255)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=15, null=True, blank=True)
    session_token = models.CharField(max_length=10, default="0")

    ROLE_CHOICES = (
        ('business', 'Business Person'),
        ('influencer', 'Influencer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='influencer')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email} ({self.role})"


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

    def __str__(self):
        return f"{self.business.name} → {self.influencer.name} ({self.status})"
