from django.urls import path
from . import views

app_name = "business"

urlpatterns = [
    path("dashboard/", views.business_dashboard, name="dashboard"),
    path("add_campaign/", views.add_campaign, name="add_profile"),
]
