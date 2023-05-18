import os
import uuid
from functools import partial

from django.db.models import Model


def upload_file_handler_path(
    base_path: str, instance: Model, filename: str
) -> str:
    """
    The function implements saving files inside a predefined path prefix,
    at the same time it replaces user uploaded file name with unique UUID name.

    The prefix is not supported by Django models itself, specifically by
    `FileField.upload_to` argument, that's why this function is going to be
    used with functools.partial.
    """
    new_filename = str(uuid.uuid4())
    if "." in filename:
        extension = filename.split(".")[-1]
        new_filename = f"{new_filename}.{extension}"
    file_path = os.path.join(base_path, new_filename)
    return file_path


def prefix_based_upload_handler(path: str) -> partial:
    """
    Wrapper for `upload_file_handler_path` which allows to specify path prefix
    where a new file should be stored.

    Example of usage:
        >>> class MyModel(models.Model)
        ...    img = models.ImageField(
        ....       upload_to=prefix_based_upload_handler('user/avatars')
        ....    )
    """
    return partial(upload_file_handler_path, base_path=path)
