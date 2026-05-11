from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in DS_LOCATIONS
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
    region: str = "Desolation Cell"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Desolation Cell Locations IDs
DC_KI_1 = 1101
DC_R_1  = 1102
DC_SK_1 = 1103



# Desolation Cell Locations
DC_LOCATIONS = [
    LocationData(
        id = DC_KI_1,
        name = "Desolation Cell: Henry's Safe Key",
        tags = {"Key Item"},
    ),
    LocationData(
        id = DC_R_1,
        name = "Desolation Cell: Chivalrous War",
        tags = {"Relic"},
    ),
    LocationData(
        id = DC_SK_1,
        name = "Desolation Cell: Starlight Skin (Bridge to Nowhere)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
]

DC_ID_TO_NAME = {
    loc.id: loc.name
    for loc in DC_LOCATIONS
}

DC_NAME_TO_ID = {
    loc.name: loc.id
    for loc in DC_LOCATIONS
}