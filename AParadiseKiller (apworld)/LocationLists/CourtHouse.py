from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in CH_LOCATIONS
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
    region: str = "Court House"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)




# Court House Locations IDs
CHC_IM_1  = 701

CHC_S_1   = 702

CHC_SK_1  = 703



# Court House Locations
CHC_LOCATIONS = [
    LocationData(
        id = CHC_IM_1,
        name = "Court House: Island Sequence Momento 020",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = CHC_S_1,
        name = "Court House: Shinji",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CHC_SK_1,
        name = "Court House: Starlight Skin (Symbols of Justice)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
]

CHC_ID_TO_NAME = {
    loc.id: loc.name
    for loc in CHC_LOCATIONS
}

CHC_NAME_TO_ID = {
    loc.name: loc.id
    for loc in CHC_LOCATIONS
}