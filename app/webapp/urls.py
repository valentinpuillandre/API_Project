from django.urls import path
from .views import LandingRegisterView

urlpatterns = [
    path("", LandingRegisterView.as_view(), name="register"),
]
