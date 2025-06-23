from django.urls import path
from django.shortcuts import redirect
from .views import (
    LandingRegisterView,
    LandingLoginView,
    AccountView,
    logout_view,
    ChatbotView
    )


def home_redirect(request):
    if request.user.is_authenticated:
        return redirect("account")
    return redirect("login")


urlpatterns = [
    path('', home_redirect, name='home'),
    path("register/", LandingRegisterView.as_view(), name="register"),
    path("login/", LandingLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("account/", AccountView.as_view(), name="account"),
    path("chatbot/", ChatbotView.as_view(), name="chatbot"),
]
