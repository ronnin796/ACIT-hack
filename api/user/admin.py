from django.contrib import admin
from .models import CustomUser , InfluencerProfile , BusinessProfile
# Register your models here.
models = [CustomUser , InfluencerProfile , BusinessProfile]
admin.site.register(models)
