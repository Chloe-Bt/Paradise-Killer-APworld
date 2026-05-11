from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in KHX_LOCATIONS
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
    region: str = "K. HX's Workshop"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# K. HX's Workshop Locations IDs
KHX_RCT_1 = 1401

KHX_ND_1  = 1402

KHX_SK_1  = 1403

KHX_WB_1  = 1404



# K. HX's Workshop Locations
KHX_LOCATIONS = [
    LocationData(
        id = KHX_RCT_1,
        name = "K. HX's Workshop: Radio Control Tower (About That...)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = KHX_ND_1,
        name = "K. HX's Workshop: Nebula Drink (Angel Nebula)",
        enabled_if = lambda options: (
            options.enable_nebula_drinks
            or options.goal == "lady_soda_dies"
        ),
        rule = lambda state, options, player: (
            not options.enable_soda_license
            or state.has("Soda License (unlock ability to buy soda cans)", player)
        ),
        tags = {"Nebula Drink"},
    ),
    LocationData(
        id = KHX_SK_1,
        name = "K. HX's Workshop: Starlight Skin (Symbols of Medication)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = KHX_WB_1,
        name = "K. HX's Workshop: Whisky Bottle (No Warning Whisky)",
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

KHX_ID_TO_NAME = {
    loc.id: loc.name
    for loc in KHX_LOCATIONS
}

KHX_NAME_TO_ID = {
    loc.name: loc.id
    for loc in KHX_LOCATIONS
}