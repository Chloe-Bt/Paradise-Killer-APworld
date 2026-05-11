from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in T_LOCATIONS
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
    region: str = "Tunnel"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Tunnel Locations IDs
T_IM_1 = 2701

T_R_1  = 2702

T_S_1  = 2703

T_C_1  = 2704



# Tunnel Locations
T_LOCATIONS = [
    LocationData(
        id = T_IM_1,
        name = "Tunnel: Island Sequence Momento 012",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = T_R_1,
        name = "Tunnel: Despairing Diary",
        tags = {"Relic"},
    ),
    LocationData(
        id = T_S_1,
        name = "Tunnel: Shinji",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = T_C_1,
        name = "Tunnel: Carving (Cosmic Deceit)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
]

T_ID_TO_NAME = {
    loc.id: loc.name
    for loc in T_LOCATIONS
}

T_NAME_TO_ID = {
    loc.name: loc.id
    for loc in T_LOCATIONS
}