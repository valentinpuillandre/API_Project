from django.urls import path

from .views import NonConformityListView, NonConformityDetailView, IndexView

urlpatterns = [
   path(
      'nonconformity/',
      NonConformityListView.as_view(),
      name='nonconformity-list'
   ),
   path(
      'nonconformity/<str:pk>/',
      NonConformityDetailView.as_view(),
      name='nonconformity-detail'
   ),
   path("", IndexView.as_view(), name="index")
]
