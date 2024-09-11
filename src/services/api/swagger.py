from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


class MobilePrivateAPISchemeGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.base_path = "/api/mobile/"
        return schema


mobile_schema_view = get_schema_view(
    openapi.Info(
        title="Mobile API documentation",
        default_version="v1",
        description="Mobile API annotation",
    ),
    urlconf="services.api.mobile.urls",
    generator_class=MobilePrivateAPISchemeGenerator,
    public=True,
    permission_classes=(AllowAny,),
)


class LoginRequiredMobileSchemaView(LoginRequiredMixin, mobile_schema_view):
    login_url = settings.SWAGGER_SETTINGS["LOGIN_URL"]
