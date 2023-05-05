from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = config["i18n"]["language_code"]

LANGUAGES = [
    ("en-us", _("English")),
]

USE_I18N = True

LOCALE_PATHS = [
    BASE_DIR / "locale",
]
