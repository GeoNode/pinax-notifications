try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError


__version__ = version("geonode-pinax-notifications")

default_app_config = "pinax.notifications.apps.AppConfig"
