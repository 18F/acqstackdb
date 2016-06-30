from django.core.management.base import BaseCommand, CommandError
from acquisitions import factories


class Command(BaseCommand):

    def handle(self, *args, **options):
        factories.ActorFactory.create_batch(5)
        # factories.AgencyFactory.create_batch(5)
        factories.SubagencyFactory.create_batch(5)
