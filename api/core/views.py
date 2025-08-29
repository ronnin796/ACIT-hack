
from django.shortcuts import render, redirect
from api.token_auth import token_login_required

def home(request):
    return render(request, 'core/home.html', {})

def signup(request):
    """
    Renders the signup page template.
    The actual signup POST request is handled via DRF.
    """
    return render(request, 'core/signup.html', {})

def login(request):
    return render(request, 'core/login.html', {})




@token_login_required
def profile_input(request):
    print("USER:", request.user, "AUTH:", request.user.is_authenticated)
    if request.user.role == 'business':
        return redirect('business:dashboard')  # Create a business dashboard
    else:
        return redirect('influencer:dashboard')  # Create an influencer dashboard
