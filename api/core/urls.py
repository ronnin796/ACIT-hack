from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.login, name='signin'),
    path('profile_input/', views.profile_input, name='profile_input'),
]