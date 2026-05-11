from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in DJY_LOCATIONS
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
    region: str = "Doom Jazz's Yacht"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Doom Jazz's Yacht Locations IDs
DJY_KI_1 = 1201



# Doom Jazz's Yacht Locations
DJY_LOCATIONS = [
    LocationData(
        id = DJY_KI_1,
        name = "Doom Jazz's Yacht: Vampire Report",
        tags = {"Key Item"},
    ),
]

DJY_ID_TO_NAME = {
    loc.id: loc.name
    for loc in DJY_LOCATIONS
}

DJY_NAME_TO_ID = {
    loc.name: loc.id
    for loc in DJY_LOCATIONS
}