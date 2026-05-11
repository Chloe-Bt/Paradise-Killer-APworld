from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in DFE_LOCATIONS
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
    region: str = "Deep Factory Entrance"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Deep Factory Locations IDs
DFE_IM_1  = 1001
DFE_IM_2  = 1002
DFE_IM_3  = 1003

DFE_KI_1  = 1004
DFE_KI_2  = 1005

DFE_R_1   = 1006

DFE_S_1   = 1007
DFE_S_2   = 1008
DFE_S_3   = 1009

DFE_C_1   = 1010
DFE_C_2   = 1011

DFE_SK_1  = 1012
DFE_SK_2  = 1013

DFE_SU_1  = 1014


# Deep Factory Entrance Locations
DFE_LOCATIONS = [
    LocationData(
        id = DFE_IM_1,
        name = "Deep Factory Entrance: Island Sequence Momento 007",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = DFE_IM_2,
        name = "Deep Factory Entrance: Island Sequence Momento 008",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = DFE_IM_3,
        name = "Deep Factory Entrance: Island Sequence Momento 009",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = DFE_KI_1,
        name = "Deep Factory Entrance: Space Helmet",
        tags = {"Key Item"},
    ),
    LocationData(
        id = DFE_KI_2,
        name = "Deep Factory Entrance: Crane System Unlock Card",
        tags = {"Key Item"},
    ),
    LocationData(
        id = DFE_R_1,
        name = "Deep Factory Entrance: Recording 003",
        enabled_if = lambda options: options.enable_recordings,
        tags = {"Recording"},
    ),
    LocationData(
        id = DFE_S_1,
        name="Deep Factory Entrance: Shinji (east warehouse)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = DFE_S_2,
        name="Deep Factory Entrance: Shinji (shore west of warehouse)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = DFE_S_3,
        name="Deep Factory Entrance: Shinji (grassy cliffs)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = DFE_C_1,
        name="Deep Factory Entrance: Carving (Blood Dancer)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = DFE_C_2,
        name="Deep Factory Entrance: Carving (Dire Rose)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = DFE_SK_1,
        name="Deep Factory Entrance: Starlight Skin (Idyllic Beach)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = DFE_SK_2,
        name="Deep Factory Entrance: Starlight Skin (Terrifying Shallows)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = DFE_SU_1,
        name = "Deep Factory Entrance: Starlight Upgrade (Worship)",
        rule = lambda state, options, player: state.count_group_unique("Nebula Soda Drinks", player) == 10,
        tags = {"Starlight Upgrade"},
    ),
]

DFE_ID_TO_NAME = {
    loc.id: loc.name
    for loc in DFE_LOCATIONS
}

DFE_NAME_TO_ID = {
    loc.name: loc.id
    for loc in DFE_LOCATIONS
}