from django.contrib import admin
from .models import CustomUser , Collaboration
# Register your models here.
models = [CustomUser , Collaboration]
admin.site.register(models)
