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
    agency = factory.SubFactory(AgencyFactory)


class ContractingOfficeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ContractingOffice

    name = factory.Faker("agency", size="small")


class ContractingOfficerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ContractingOfficer

    name = factory.Faker("name")
    if len(models.ContractingOffice.objects.all()) > 2:
        contracting_office = factory.Iterator(
            models.ContractingOffice.objects.all()
        )
    else:
        contracting_office = factory.SubFactory(ContractingOfficeFactory)


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


class ActorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Actor

    name = factory.Faker("company")


class StepFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Step

    if len(models.Stage.objects.all()) > 3:
        stage = factory.Iterator(
            models.Stage.objects.all()
        )
    else:
        stage = factory.SubFactory(StageFactory)
    if len(models.Actor.objects.all()) > 3:
        actor = factory.Iterator(
            models.Actor.objects.all()
        )
    else:
        actor = factory.SubFactory(ActorFactory)


class StepTrackThroughFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.StepTrackThroughModel

    step = factory.SubFactory(StepFactory)
    if len(models.Track.objects.all()) > 1:
        track = factory.Iterator(
            models.Track.objects.all()
        )
    else:
        track = factory.SubFactory(TrackFactory)


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
    if len(models.Step.objects.all()) > 5:
        step = factory.Iterator(
            models.Step.objects.all()
        )
    else:
        step = factory.SubFactory(StepFactory)
    if len(models.Subagency.objects.all()) > 2:
        subagency = factory.Iterator(
            models.Subagency.objects.all()
        )
    else:
        subagency = factory.SubFactory(SubagencyFactory)
    if len(models.Track.objects.all()) > 0:
        track = factory.Iterator(
            models.Track.objects.all()
        )
    else:
        track = factory.SubFactory(TrackFactory)


class EvaluatorFactory(factory.django.DjangoModelFactory):
    pass


class ReleaseFactory(factory.django.DjangoModelFactory):
    pass
