# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
import random

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, default='Anonymous', null=True, blank=True)
    email = models.EmailField(unique=True, max_length=255)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    image = models.ImageField(upload_to='user/', blank=True, null=True)
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







def random_followers():
    return random.randint(1000, 100000)

def random_engagement_rate():
    return round(random.uniform(0.5, 10.0), 2)

class InfluencerProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="influencer_profile"
    )
    
    niche = models.CharField(max_length=100)  
    platforms = models.JSONField(default=list)
    image = models.ImageField(upload_to='Influencer/', blank=True, null=True)
    followers = models.PositiveIntegerField(default=random_followers)
    engagement_rate = models.FloatField(default=random_engagement_rate)
    audience_age = models.JSONField(default=list)  
    audience_location = models.CharField(max_length=100, default="Global")

    positive_reviews = models.PositiveIntegerField(default=0)
    negative_reviews = models.PositiveIntegerField(default=0)

    def review(self, positive=True):
        if positive:
            self.positive_reviews += 1
        else:
            self.negative_reviews += 1
        self.save()


class BusinessProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="business_profiles")
    
    business_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='BusinessProfile/', blank=True, null=True)
    industry = models.CharField(max_length=100)            
    target_platforms = models.JSONField(default=list)  
    budget = models.PositiveIntegerField(default=0)
    target_age = models.JSONField(default=list)        
    target_location = models.CharField(max_length=100, default="Global")

 
