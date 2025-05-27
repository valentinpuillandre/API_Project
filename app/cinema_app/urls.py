from django.urls import path

from . import views

urlpatterns = [
   path(
      'nonconformity/',
      views.NonConformityViewSet.as_view(),
      name='nonconformity'
   ),
   path("", views.index, name="index")
]
