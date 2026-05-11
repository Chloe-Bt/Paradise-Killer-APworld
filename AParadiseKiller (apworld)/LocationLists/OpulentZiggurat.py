from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in OZ_LOCATIONS
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
    region: str = "Opulent Ziggurat"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Opulent Ziggurat Locations IDs
OZ_IM_1 = 1701

OZ_ND_1 = 1702

OZ_R_1  = 1703
OZ_R_2  = 1704
OZ_R_3  = 1705

OZ_S_1  = 1706

OZ_C_1  = 1707
OZ_C_2  = 1708
OZ_C_3  = 1709
OZ_C_4  = 1710
OZ_C_5  = 1711

OZ_SK_1 = 1712
OZ_SK_2 = 1713



# Opulent Ziggurat Locations
OZ_LOCATIONS = [
    LocationData(
        id = OZ_IM_1,
        name = "Opulent Ziggurat: Island Sequence Momento 014",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = OZ_ND_1,
        name = "Opulent Ziggurat: Nebula Drink (Statue Mind)",
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
        id = OZ_R_1,
        name = "Opulent Ziggurat: Lucky Doll",
        tags = {"Relic"},
    ),
    LocationData(
        id = OZ_R_2,
        name = "Opulent Ziggurat: Time Worn Blood Bowl",
        tags = {"Relic"},
    ),
    LocationData(
        id = OZ_R_3,
        name = "Opulent Ziggurat: Faulty Worship Stamp",
        tags = {"Relic"},
    ),
    LocationData(
        id = OZ_S_1,
        name = "Opulent Ziggurat: Shinji",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = OZ_C_1,
        name = "Opulent Ziggurat: Carving (Moonlight Petal)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = OZ_C_2,
        name = "Opulent Ziggurat: Carving (Shadow Zero)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = OZ_C_3,
        name = "Opulent Ziggurat: Carving (Vile Embrace)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = OZ_C_4,
        name = "Opulent Ziggurat: Carving (Beautiful Spectre)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = OZ_C_5,
        name = "Opulent Ziggurat: Carving (Destroyed Eden)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = OZ_SK_1,
        name = "Opulent Ziggurat: Starlight Skin (Inverted Pyramid)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = OZ_SK_2,
        name = "Opulent Ziggurat: Starlight Skin (Holy Refinery)",
        enabled_if = lambda options: options.enable_starlight_skins,
        rule = lambda state, options, player: (
            state.has("LLD Upgrade: Air Dash", player)
            and state.has("LLD Upgrade: Double Jump", player)
        ),
        tags = {"Starlight Skin"},
    ),
]

OZ_ID_TO_NAME = {
    loc.id: loc.name
    for loc in OZ_LOCATIONS
}

OZ_NAME_TO_ID = {
    loc.name: loc.id
    for loc in OZ_LOCATIONS
}