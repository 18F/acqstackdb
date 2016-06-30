import factory
from acquisitions import models
from acquisitions.providers.fake_agency import AgencyProvider

factory.Faker.add_provider(AgencyProvider)


class AgencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Agency

    name = factory.Faker("agency")


class SubagencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Subagency

    name = factory.Faker("agency")
    agency = factory.SubFactory(AgencyFactory)


class ContractingOfficeFactory(factory.django.DjangoModelFactory):
    pass


class ContractingOfficerFactory(factory.django.DjangoModelFactory):
    pass


class CORFactory(factory.django.DjangoModelFactory):
    pass


class TrackFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Track

    name = factory.Faker("bs")


class StageFactory(factory.django.DjangoModelFactory):
    pass


class StepFactory(factory.django.DjangoModelFactory):
    pass


class ActorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Actor

    name = factory.Faker("company")


class VendorFactory(factory.django.DjangoModelFactory):
    pass


class RoleFactory(factory.django.DjangoModelFactory):
    pass


class AcquisitionFactory(factory.django.DjangoModelFactory):
    pass


class EvaluatorFactory(factory.django.DjangoModelFactory):
    pass


class ReleaseFactory(factory.django.DjangoModelFactory):
    pass
