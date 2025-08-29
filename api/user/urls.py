from unittest.mock import patch
from rest_framework import routers
from . import views
from django.urls import path, include
router = routers.DefaultRouter()
router.register(r'user',views.UserViewSet , basename = 'user')
router.register(r'influencer-profile',views.InfluencerProfileViewSet , basename = 'influencer-profile')
router.register(r'business-profile',views.BusinessProfileViewSet , basename = 'business-profile')

urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.signin , name='login'),
    path('logout/<int:id>/',views.signout , name='signout'),
   

]