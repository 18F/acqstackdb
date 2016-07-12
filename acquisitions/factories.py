import factory
from acquisitions import models
from acquisitions.providers import fake_agency

factory.Faker.add_provider(fake_agency.AgencyProvider)


def iterate_or_create(model, limit, subfactory):
    if len(model.objects.all()) > limit:
        return factory.Iterator(model.objects.all())
    else:
        return factory.SubFactory(subfactory)


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
    contracting_office = iterate_or_create(
        models.ContractingOffice,
        2,
        ContractingOfficeFactory
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

    stage = iterate_or_create(
        models.Stage,
        3,
        StageFactory
    )
    actor = iterate_or_create(
        models.Actor,
        3,
        ActorFactory
    )


class StepTrackThroughFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.StepTrackThroughModel

    step = factory.SubFactory(StepFactory)
    track = iterate_or_create(
        models.Track,
        1,
        TrackFactory
    )
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
    step = iterate_or_create(
        models.Step,
        5,
        StepFactory
    )
    subagency = iterate_or_create(
        models.Subagency,
        2,
        SubagencyFactory
    )
    track = iterate_or_create(
        models.Track,
        0,
        TrackFactory
    )


class EvaluatorFactory(factory.django.DjangoModelFactory):
    pass


class ReleaseFactory(factory.django.DjangoModelFactory):
    pass
