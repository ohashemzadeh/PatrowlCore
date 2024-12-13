
from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view for Swagger and Redoc
schema_view = get_schema_view(
    openapi.Info(
        title="PatrowlCore API",
        default_version="v1",
        description="API documentation for PatrowlCore",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('api.urls')),  # Include the API app's URLs

]
