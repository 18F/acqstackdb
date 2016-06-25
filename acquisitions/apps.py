from django.apps import AppConfig


class AwardStatusConfig(AppConfig):
    name = 'acquisitions'
    verbose_name = 'Acquisitions'

    def ready(self):
        from . import signals
