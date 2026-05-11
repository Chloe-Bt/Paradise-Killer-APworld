from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in PG_LOCATIONS
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
    region: str = "Paradise Gates"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Paradise Gates Locations IDs
PG_KI_1 = 1901

PG_C_1  = 1902

PG_W_1  = 1903



# Paradise Gates Locations
PG_LOCATIONS = [
    LocationData(
        id = PG_KI_1,
        name = "Paradise Gates: Death Scream Device",
        tags = {"Key Item"},
    ),
    LocationData(
        id = PG_C_1,
        name = "Paradise Gates: Carving (Zealous)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = PG_W_1,
        name = "Paradise Gates: Whisky Bottle (Hair Trigger Whisky)",
        enabled_if = lambda options: (
            options.enable_whisky_bottles
            or options.goal == "lady_whisky_dies"
        ),
        rule = lambda state, options, player: (
            not options.enable_alcohol_license
            or state.has("Alcohol License (unlock ability to get whisky bottles)", player)
        ),
        tags = {"Whisky Bottle"},
    ),
]

PG_ID_TO_NAME = {
    loc.id: loc.name
    for loc in PG_LOCATIONS
}

PG_NAME_TO_ID = {
    loc.name: loc.id
    for loc in PG_LOCATIONS
}