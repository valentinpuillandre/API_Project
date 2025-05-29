from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from rest_framework_simplejwt.tokens import RefreshToken


class LandingRegisterView(View):
    def get(self, request):
        return render(request, "webapp/register.html")

    def post(self, request):
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        errors = []
        if not username or not email or not password1 or not password2:
            errors.append("All fields are required.")
        if password1 != password2:
            errors.append("Passwords do not match.")
        if User.objects.filter(username=username).exists():
            errors.append("Username already taken.")
        if User.objects.filter(email=email).exists():
            errors.append("Email already registered.")
        if errors:
            return render(request, "webapp/register.html", {"errors": errors})
        User.objects.create_user(
            username=username, email=email, password=password1
            )
        messages.success(
            request,
            "Account created successfully. Please log in."
            )
        return redirect("register")


class LandingLoginView(View):
    def get(self, request):
        return render(request, "webapp/login.html")

    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("account")
        return render(
            request,
            "webapp/login.html",
            {"error": "Invalid credentials."}
            )


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")


@method_decorator(login_required, name="dispatch")
class AccountView(View):
    def get(self, request):
        # Generate JWT token for the current user
        refresh = RefreshToken.for_user(request.user)
        jwt_token = str(refresh.access_token)
        return render(
            request,
            "webapp/account.html",
            {"jwt_token": jwt_token}
        )

    def post(self, request):
        request.user.delete()
        logout(request)
        messages.success(request, "Account deleted.")
        return redirect("register")
