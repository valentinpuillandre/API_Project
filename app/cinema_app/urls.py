from django.urls import path

from . import views

urlpatterns = [
   path('viewers/', views.ViewersView.as_view(), name='viewers'),
   path("", views.index, name="index")
]
