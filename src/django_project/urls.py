from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.ENVIRONMENT == settings.ENVIRONMENT_LOCAL:
    # enabling media files serving for local env
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


if settings.ENVIRONMENT not in [
    settings.ENVIRONMENT_PROD,
    settings.ENVIRONMENT_STAGE,
]:
    # enabling drf auth for swagger in case it's not stage/production env
    urlpatterns += static(
        "rest-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    )
