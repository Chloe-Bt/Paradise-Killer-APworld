#Syndicate Graveyard
SG_ID_TO_NAME = {}
ALL_SG = list(SG_ID_TO_NAME.keys())

from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in SGLOCATIONS
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
    region: str = "Syndicate Graveyard"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Syndicate Graveyard Locations IDs
SG_KI_1 = 2501
SG_KI_2 = 2502

SG_ND_1 = 2503

SH_R_1  = 2504

SH_S_1  = 2505

SH_SK_1 = 2506



# Syndicate Graveyard Locations
SG_LOCATIONS = [
    LocationData(
        id = SG_KI_1,
        name = "Syndicate Graveyard: Eyes Kiwami's Blood Vial",
        rule = lambda state, options, player: (
            state.has("Starlight Upgrade: Worship", player)
            and state.has("Starlight Upgrade: Pyramids", player)
        ),
        tags = {"Key Item"},
    ),
    LocationData(
        id = SG_KI_2,
        name = "Syndicate Graveyard: Grace Bloodlines' Blood Vial",
        rule = lambda state, options, player: state.has("Starlight Upgrade: Cosmos", player),
        tags = {"Key Item"},
    ),
    LocationData(
        id = SG_ND_1,
        name = "Syndicate Graveyard: Nebula Drink (The Elusive Chocolate)",
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
        id = SH_R_1,
        name = "Syndicate Graveyard: Vintage Watch",
        tags = {"Relic"},
    ),
    LocationData(
        id = SH_S_1,
        name = "Syndicate Graveyard: Shinji",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = SH_SK_1,
        name = "Syndicate Graveyard: Starlight Skin (Symbols of Secrets)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
]

SG_ID_TO_NAME = {
    loc.id: loc.name
    for loc in SG_LOCATIONS
}

SG_NAME_TO_ID = {
    loc.name: loc.id
    for loc in SG_LOCATIONS
}