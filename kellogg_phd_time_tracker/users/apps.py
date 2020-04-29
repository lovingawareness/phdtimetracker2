from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "kellogg_phd_time_tracker.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import kellogg_phd_time_tracker.users.signals  # noqa F401
        except ImportError:
            pass
