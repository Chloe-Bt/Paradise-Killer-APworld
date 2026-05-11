MB_ID_TO_NAME = {}
ALL_MB = list(MB_ID_TO_NAME.keys())

from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in MB_LOCATIONS
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
    region: str = "Marshal Barracks"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Marshal Barracks Locations IDs
MB_C_1 = 1501



# Marshal Barracks Locations
MB_LOCATIONS = [
    LocationData(
        id = MB_C_1,
        name = "Marshal Barracks: Carving (New Night)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
]

MB_ID_TO_NAME = {
    loc.id: loc.name
    for loc in MB_LOCATIONS
}

MB_NAME_TO_ID = {
    loc.name: loc.id
    for loc in MB_LOCATIONS
}