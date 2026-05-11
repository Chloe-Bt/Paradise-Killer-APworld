from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in P_LOCATIONS
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
    region: str = "Pyramid"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Pyramid Locations IDs
P_S_1 = 2001



# Pyramid Locations
P_LOCATIONS = [
    LocationData(
        id = P_S_1,
        name = "Pyramid: Shinji",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
]

P_ID_TO_NAME = {
    loc.id: loc.name
    for loc in P_LOCATIONS
}

P_NAME_TO_ID = {
    loc.name: loc.id
    for loc in P_LOCATIONS
}