from unittest.mock import patch
from rest_framework import routers
from . import views
from django.urls import path, include
router = routers.DefaultRouter()
router.register(r'user',views.UserViewSet , basename = 'user')
router.register(r'collaborations' , views.CollaborationViewSet , basename = 'collaboration') 

urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.signin , name='signin'),
    path('logout/<int:id>/',views.signout , name='signout'),
   

]