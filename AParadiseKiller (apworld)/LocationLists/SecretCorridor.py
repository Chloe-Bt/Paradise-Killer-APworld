from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in SC_LOCATIONS
        if loc.enabled_if <= enabled_settings
    ]

def get_location_ids(enabled_settings: set[str]):
    return [
        loc.id
        for loc in get_enabled_locations(enabled_settings)
    ]



@dataclass(frozen=True)
class LocationData:
    id: int
    name: str

    # Optional metadata
    region: str = "Secret Corridor"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Secret Corridor Locations IDs
SC_KI_1 = 2301
SC_KI_2 = 2302


# Secret Corridor Locations
SC_LOCATIONS = [
    LocationData(
        id = SC_KI_1,
        name="Secret Corridor: Corridor Key",
        tags = {"Key Item"},
    ),
    LocationData(
        id = SC_KI_2,
        name="Secret Corridor: Dainonigate's Blood Sample",
        tags = {"Key Item"},
    ),
]

SC_ID_TO_NAME = {
    loc.id: loc.name
    for loc in SC_LOCATIONS
}

SC_NAME_TO_ID = {
    loc.name: loc.id
    for loc in SC_LOCATIONS
}