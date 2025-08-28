# urls.py
from rest_framework.routers import DefaultRouter
from .views import CollaborationViewSet , RecommendationView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'',CollaborationViewSet)

urlpatterns = [
   
    path('', include(router.urls)),
    path('recommendations/<int:business_id>/', RecommendationView.as_view(), name='recommendations'),
    
    
]