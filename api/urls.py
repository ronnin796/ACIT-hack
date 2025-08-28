from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
   
    
    path('user/',include('api.user.urls')),

    path('api-token-auth/' , views.obtain_auth_token , name='api_token_auth'),
    
]
