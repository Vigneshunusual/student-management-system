from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('api/auth/', include('accounts.urls')),

    # APIs
    path('api/students/', include('students.urls')),
    path('api/departments/', include('departments.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/library-cards/', include('library.urls')),

    # OpenAPI schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
]