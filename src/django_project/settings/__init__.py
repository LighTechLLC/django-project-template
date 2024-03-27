import tomllib
from pathlib import Path

from split_settings.tools import include as settings_include
from split_settings.tools import optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# toml config file set up
CONFIG_FILE = BASE_DIR / "config.toml"

# using `default_config.toml` file in case `config.toml` does not exist
if not CONFIG_FILE.exists():
    CONFIG_FILE = BASE_DIR / "default_config.toml"

# loading configuration from the toml config file
with open(CONFIG_FILE, "rb") as f:
    config = tomllib.load(f)

# list of supported environments
ENVIRONMENT_LOCAL = "local"
ENVIRONMENT_STAGE = "stage"
ENVIRONMENT_DEV = "dev"
ENVIRONMENT_PROD = "production"
SUPPORTED_ENVIRONMENTS = [
    ENVIRONMENT_LOCAL,
    ENVIRONMENT_STAGE,
    ENVIRONMENT_DEV,
    ENVIRONMENT_PROD,
]

# currently used environment
ENVIRONMENT = config["base"]["environment"]

if ENVIRONMENT not in SUPPORTED_ENVIRONMENTS:
    raise ValueError(f"Unsupported environment: ENVIRONMENT={ENVIRONMENT}")

# including setting components
settings_include(
    "common.py",
    "installed_apps.py",
    "auth.py",
    "database.py",
    "i18n.py",
    "tz.py",
    "storage.py",
    "rest.py",
    "swagger.py",
    "celery.py",
    "email.py",
    "logging.py",
    "tests.py",
    "sentry.py",
    optional("local_settings.py"),
)
