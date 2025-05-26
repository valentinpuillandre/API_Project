from django.urls import path

from . import views

urlpatterns = [
   path('viewers/', views.ViewersView.as_view(), name='viewers'),
   path(
      'nonconformity/',
      views.NonConformityViewSet.as_view(),
      name='nonconformity'
   ),
   path("", views.index, name="index")
]
