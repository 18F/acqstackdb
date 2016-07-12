from django.core.management.base import BaseCommand, CommandError
from acquisitions import factories


class Command(BaseCommand):

    def handle(self, *args, **options):
        factories.ActorFactory.create_batch(5)
        factories.AgencyFactory.create_batch(5)
        factories.SubagencyFactory.create_batch(10)
        factories.ContractingOfficeFactory.create_batch(2)
        factories.ContractingOfficerFactory.create_batch(10)
        factories.CORFactory.create_batch(10)
        factories.TrackFactory.create_batch(3)
        factories.StageFactory.create_batch(6)
        factories.StepFactory.create_batch(10)
        factories.StepTrackThroughFactory.create_batch(30)
        factories.AcquisitionFactory.create_batch(50)
