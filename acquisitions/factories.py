import factory
from acquisitions import models
from acquisitions.providers import fake_agency

factory.Faker.add_provider(fake_agency.AgencyProvider)


class AgencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Agency

    name = factory.Faker("agency")


class SubagencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Subagency

    name = factory.Faker("agency", size="medium")
    agency = factory.Iterator(models.Agency.objects.all())


class ContractingOfficeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ContractingOffice

    name = factory.Faker("agency", size="small")


class ContractingOfficerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ContractingOfficer

    name = factory.Faker("name")
    contracting_office = factory.Iterator(
        models.ContractingOffice.objects.all()
    )


class CORFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.COR

    name = factory.Faker("name")


class TrackFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Track

    name = factory.Faker("bs")


class StageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Stage

    name = factory.Faker("bs")
    wip_limit = factory.Faker("random_digit_not_null")


class ActorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Actor

    name = factory.Faker("company")


class StepFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Step

    stage = factory.Iterator(models.Stage.objects.all())
    actor = factory.Iterator(models.Actor.objects.all())


class StepTrackThroughFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.StepTrackThroughModel

    step = factory.Iterator(models.Step.objects.all())
    track = factory.Iterator(models.Track.objects.all())
    wip_limit = factory.Faker("random_digit_not_null")


class TrackWithStepFactory(TrackFactory):
    together = factory.RelatedFactory(StepTrackThroughFactory, 'track')


class VendorFactory(factory.django.DjangoModelFactory):
    pass


class RoleFactory(factory.django.DjangoModelFactory):
    pass


class AcquisitionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Acquisition

    task = factory.Faker("catch_phrase")
    step = factory.Iterator(models.Step.objects.all())
    subagency = factory.Iterator(models.Subagency.objects.all())
    track = factory.Iterator(models.Track.objects.all())


class EvaluatorFactory(factory.django.DjangoModelFactory):
    pass


class ReleaseFactory(factory.django.DjangoModelFactory):
    pass
