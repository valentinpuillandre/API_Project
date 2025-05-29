from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    NonConformityListView,
    NonConformityDetailView,
    NonConformityStatsView,
    IndexView
)

schema_view = get_schema_view(
    openapi.Info(
        title="API Project",
        default_version="v1",
        description="API documentation for the project.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
      path("", IndexView.as_view(), name="index"),
      path(
         "swagger/",
         schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"
      ),
      path(
         "redoc/",
         schema_view.with_ui("redoc", cache_timeout=0),
         name="schema-redoc"
      ),
      path(
         'token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'
      ),
      path(
         'token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'
      ),

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
      path(
         'nonconformity/stats/severity/',
         NonConformityStatsView.as_view(),
         name='nonconformity-stats-severity'
      ),

]
