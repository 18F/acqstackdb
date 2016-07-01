import random
from faker.providers import BaseProvider


class AgencyProvider(BaseProvider):
    agency_parts = (
        (
            "Department of", "Office of", "Bureau of",
        ),
        (
            "the Interior", "Administrating", "Hats", "Management", "Labor",
            "Finance", "Departments", "Flying"
        )
    )

    big_agency_start = (
        "Department of", "Office of", "Bureau of",
    )

    big_agency_end = (
        "Administration", "Agency",
    )

    medium_agency_end = (
        "Division", "Section",
    )

    small_agency_end = (
        "Region", "Office", "Room",
    )

    extra_parts = (
        "Synergy", "Failure", "High-Profile Success", "First Aid", "Gravy",
        "Sandwiches", "Wine", "Budget", "Style"
    )

    def agency(self, size="large"):
        result = []
        for part in self.agency_parts:
            result.append(self.random_element(part))
        if random.randint(0, 100) > 70:
            result.append("and")
            result.append(self.random_element(self.extra_parts))

        return " ".join(result)
