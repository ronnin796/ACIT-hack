from django.shortcuts import redirect
from functools import wraps
from api.user.models import CustomUser


def token_login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        token = request.GET.get('session_token') or request.POST.get('session_token')
        try:
            user = CustomUser.objects.get(session_token=token)
            request.user = user
        except CustomUser.DoesNotExist:
            return redirect('signin')
        return view_func(request, *args, **kwargs)
    return _wrapped_view