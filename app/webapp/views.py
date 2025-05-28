from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View


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
