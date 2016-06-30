from django.core.management.base import BaseCommand, CommandError
from acquisitions import factories


class Command(BaseCommand):

    def handle(self, *args, **options):
        factories.ActorFactory.create_batch(5)
        factories.SubagencyFactory.create_batch(5)
        factories.ContractingOfficerFactory.create_batch(5)
        factories.CORFactory.create_batch(5)
        factories.TrackWithStepFactory.create_batch(2)
        factories.AcquisitionFactory.create_batch(10)
