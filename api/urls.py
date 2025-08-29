from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path("business/", include(('api.business.urls', 'business'), namespace='business')),
    
    path("user/", include(('api.user.urls', 'user'), namespace='user')),
    path("collabs/", include(('api.collabs.urls', 'collabs'), namespace='collabs')),
    path("api-token-auth/", views.obtain_auth_token, name="api_token_auth"),
]
    