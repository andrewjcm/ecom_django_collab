from contrib.views import char_count
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("admin/", admin.site.urls),
    path("char_count", char_count, name="char_count"),
    re_path(".*", TemplateView.as_view(template_name="index.html")),
]
