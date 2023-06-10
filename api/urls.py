from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include

from .views import *

urlpatterns = [
    path('url/<uuid:id>/', URLView.as_view({'get': 'get', 'put': 'put', 'delete': 'delete'})),
    path('url/', URLView.as_view({'post': 'post'})),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
