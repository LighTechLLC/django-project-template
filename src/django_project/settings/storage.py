STATIC_URL = config["storage"]["static_url"]
MEDIA_URL = config["storage"]["media_url"]

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_ROOT = config["storage"]["media_root"]
STATIC_ROOT = config["storage"]["static_root"]

# there should be listed all paths which used in project
FILE_FOLDERS = {
    # "avatars": Path("users/avatars"),
}
