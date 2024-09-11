from django.conf import settings
from django.urls import include, path

from services.api.mobile.urls import urlpatterns as mobile_urls
from services.api.swagger import LoginRequiredMobileSchemaView

app_name = "api"

urlpatterns = [
    path("mobile/", include((mobile_urls, "mobile"), namespace="mobile")),
]

if settings.ENVIRONMENT not in [
    settings.ENVIRONMENT_PROD,
    settings.ENVIRONMENT_STAGE,
]:
    urlpatterns += [
        path("mobile/doc.yaml", LoginRequiredMobileSchemaView.without_ui()),
        path(
            "mobile/doc/",
            LoginRequiredMobileSchemaView.with_ui("swagger", cache_timeout=0),
        ),
    ]
