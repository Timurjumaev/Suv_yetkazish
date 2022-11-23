"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Suv_yetkazish",
      default_version='v1',
      description="This is description for this site",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="tjumaev2002@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('suvlar/', SuvlarAPIView.as_view()),
    path('suv/<int:pk>/', SuvAPIView.as_view()),
    path('mijozlar/', MijozlarAPIView.as_view()),
    path('mijoz/<int:pk>/', MijozAPIView.as_view()),
    path('buyurtmalar/', BuyurtmalarAPIView.as_view()),
    path('adminlar/', AdminlarAPIView.as_view()),
    path('admin2/<int:pk>/', AdminAPIView.as_view()),
    path('haydovchilar/', HaydovchilarAPIView.as_view()),
    path('haydovchi/<int:pk>/', HaydovchiAPIView.as_view()),
    path('access/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0)),
    path('redoc/', schema_view.with_ui("redoc", cache_timeout=0)),
]
