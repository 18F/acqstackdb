import random
from faker.providers import BaseProvider


class AgencyProvider(BaseProvider):
    big_agency_parts = (
        (
            "Department of", "Office of", "Bureau of"
        ),
        (
            "the Interior", "Administrating", "Hats", "Management", "Labor",
            "Finance", "Departments", "Flying"
        )
    )

    medium_agency_parts = ()

    small_agency_parts = ()

    extra_parts = (
        "Synergy", "Failure", "High-Profile Success", "First Aid", "Gravy",
        "Sandwiches", "Wine", "Budget", "Style"
    )

    def agency(self, size="large"):
        result = []
        for part in self.big_agency_parts:
            result.append(self.random_element(part))
        if random.randint(0, 100) > 70:
            result.append("and")
            result.append(self.random_element(self.extra_parts))

        return " ".join(result)
