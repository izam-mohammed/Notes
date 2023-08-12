from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Configuration class for the 'core' app.

    Attributes:
    - default_auto_field (str): Specifies the default primary key field type for models.
    - name (str): Specifies the name of the app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
