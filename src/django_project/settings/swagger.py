from django.urls import reverse_lazy

SWAGGER_SETTINGS = {
    "LOGIN_URL": reverse_lazy("api:rest_framework:login"),
    "LOGOUT_URL": reverse_lazy("api:rest_framework:logout"),
    "USE_SESSION_AUTH": True,
}
