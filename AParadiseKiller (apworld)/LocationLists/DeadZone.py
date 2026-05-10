from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in DZ_LOCATIONS
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
    region: str = "Dead Zone"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Idle Lands Locations IDs
DZ_IM_1  = 901
DZ_IM_2  = 902

DZ_ND_1  = 903

DZ_S_1   = 904

DZ_C_1   = 905

DZ_WB_1  = 906



# Dead Zone Locations
DZ_LOCATIONS = [
    LocationData(
        id = DZ_IM_1,
        name="Dead Zone: Island Sequence Momento 016",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = DZ_IM_2,
        name="Dead Zone: Island Sequence Momento 017",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = DZ_ND_1,
        name="Dead Zone: Nebula Drink (Blood Fountain)",
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
        id = DZ_S_1,
        name="Dead Zone: Shinji",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = DZ_C_1,
        name="Dead Zone: Carving (Dying from Sadness)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = DZ_WB_1,
        name="Dead Zone: Whisky Bottle (Winning Devil Whisky)",
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
DZ_ID_TO_NAME = {
    loc.id: loc.name
    for loc in DZ_LOCATIONS
}

DZ_NAME_TO_ID = {
    loc.name: loc.id
    for loc in DZ_LOCATIONS
}