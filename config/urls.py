from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("apps.users.api.v1.urls")),
    path('api/v1/payments/', include('apps.payments.api.v1.urls')),
]
