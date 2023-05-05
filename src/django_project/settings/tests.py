import sys

if "test" in sys.argv:
    # Change settings for tests
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        }
    }
