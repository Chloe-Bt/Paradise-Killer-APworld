from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in MG_LOCATIONS
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
    region: str = "Mountain Gorge"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)




# Mountain Gorge Locations IDs
MG_IM_1  = 1601
MG_IM_2  = 1602

MG_RCT_1 = 1603

MG_ND_1  = 1604

MG_RC_1  = 1605
MG_RC_2  = 1606

MG_S_1   = 1607
MG_S_2   = 1608
MG_S_3   = 1609
MG_S_4   = 1610

MG_WB_1  = 1611


# Mountain Gorge Locations
MG_LOCATIONS = [
    LocationData(
        id = MG_IM_1,
        name = "Mountain Gorge: Island Sequence Momento 013",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = MG_IM_2,
        name = "Mountain Gorge: Island Sequence Momento 021",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = MG_RCT_1,
        name = "Mountain Gorge: Radio Control Tower (Midori Eyes)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = MG_ND_1,
        name = "Mountain Gorge: Nebula Drink (Dead Moon)",
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
        id = MG_RC_1,
        name = "Mountain Gorge: Recording 001",
        enabled_if = lambda options: options.enable_recordings,
        tags = {"Recording"},
    ),
    LocationData(
        id = MG_RC_2,
        name = "Mountain Gorge: Recording 002",
        enabled_if = lambda options: options.enable_recordings,
        tags = {"Recording"},
    ),
    LocationData(
        id = MG_S_1,
        name = "Mountain Gorge: Shinji (large Silent Goat statue)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = MG_S_2,
        name = "Mountain Gorge: Shinji (Below Foot Bath)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = MG_S_3,
        name = "Mountain Gorge: Shinji (lower foundations)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = MG_S_4,
        name = "Mountain Gorge: Shinji (rocky cliffs overlooking path)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = MG_WB_1,
        name = "Mountain Gorge: Whisky Bottle (Dead Man's Ambitious Whisky)",
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

MG_ID_TO_NAME = {
    loc.id: loc.name
    for loc in MG_LOCATIONS
}

MG_NAME_TO_ID = {
    loc.name: loc.id
    for loc in MG_LOCATIONS
}