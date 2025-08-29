from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api.user.models import BusinessProfile, CustomUser
from api.collabs.models import Collaboration
from api.collabs.recommendations import recommend_influencers
from api.user.serializers import InfluencerProfileSerializer
from api.token_auth import token_login_required


@token_login_required
def business_dashboard(request):
    # Get all business profiles of this user
    business_profiles = BusinessProfile.objects.filter(user=request.user)

    # Get all collaborations where this business sent the request
    collaborations = Collaboration.objects.filter(business=request.user).order_by('-created_at')

    # Build recommendations per business profile
    recommendations_by_profile = {}
    for profile in business_profiles:
        recommended = recommend_influencers(profile, top_n=5)
        recommendations_by_profile[profile.id] = recommended

    context = {
        "business_profiles": business_profiles,
        "collaborations": collaborations,
        "recommendations_by_profile": recommendations_by_profile,
    }
    return render(request, "business/business_dashboard.html", context)


def add_campaign(request):
    if request.method == "POST":
        # Process form data here to create a new campaign
        # For simplicity, let's assume we just redirect to the dashboard after "adding" a campaign
        return redirect("business:dashboard")
    
    return render(request, "business/add_profile.html", {})
