import factory
import random
from faker import Faker
from faker.providers import BaseProvider
from acquisitions import models

fake = Faker()


class AgencyProvider(BaseProvider):
    agency_parts = (
        (
            "Department of", "Office of", "Bureau of"
        ),
        (
            "the Interior", "Administrating", "Hats", "Management", "Labor",
            "Finance", "Departments", "Flying"
        )
    )

    extra_parts = (
        "Synergy", "Failure", "High-Profile Success", "First Aid", "Gravy",
        "Sandwiches", "Wine", "Budget", "Style"
    )

    def agency(self):
        result = []
        for part in self.agency_parts:
            result.append(self.random_element(part))
        if random.randint(0, 100) > 70:
            result.append("and")
            result.append(self.random_element(self.extra_parts))

        return " ".join(result)

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


class AcquisitionFactory(factory.django.DjangoModelFactory):
    pass
