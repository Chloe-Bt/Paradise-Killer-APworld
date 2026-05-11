#Syndicate HQ
SHQ_ID_TO_NAME = {}
ALL_SHQ = list(SHQ_ID_TO_NAME.keys())

from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in SHQ_LOCATIONS
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
    region: str = "Syndicate HQ"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Syndicate HQ Locations IDs
SHQ_IM_1  = 2601
SHQ_IM_2  = 2602

SHQ_KI_1  = 2603
SHQ_KI_2  = 2604
SHQ_KI_3  = 2605
SHQ_KI_4  = 2606
SHQ_KI_5  = 2607
SHQ_KI_6  = 2608
SHQ_KI_7  = 2609
SHQ_KI_8  = 2610
SHQ_KI_9  = 2611
SHQ_KI_10 = 2612
SHQ_KI_11 = 2613

SHQ_RCT_1 = 2614
SHQ_RCT_2 = 2615

SHQ_ND_1  = 2616

SHQ_S_1   = 2617
SHQ_S_2   = 2618
SHQ_S_3   = 2619

SHQ_C_1   = 2620

SHQ_SK_1  = 2621
SHQ_SK_2  = 2622
SHQ_SK_3  = 2623



# Syndicate HQ Locations
SHQ_LOCATIONS = [
    LocationData(
        id = SHQ_IM_1,
        name = "Syndicate HQ: Island Sequence Momento 001",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = SHQ_IM_2,
        name = "Syndicate HQ: Island Sequence Momento 002",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = SHQ_KI_1,
        name = "Syndicate HQ: red crest 1/10",
        tags = {"Key Item"},
    ),
    LocationData(
        id = SHQ_KI_2,
        name = "Syndicate HQ: red crest 2/10",
        tags = {"Key Item"},
    ),
    LocationData(
        id = SHQ_KI_3,
        name = "Syndicate HQ: red crest 3/10",
        tags = {"Key Item"},
    ),
    LocationData(
        id = SHQ_KI_4,
        name = "Syndicate HQ: red crest 4/10",
        tags = {"Key Item"},
    ),
    LocationData(
        id = SHQ_KI_5,
        name = "Syndicate HQ: red crest 5/10",
        tags = {"Key Item"},
    ),
    LocationData(
        id = SHQ_KI_6,
        name = "Syndicate HQ: red crest 6/10",
        tags = {"Key Item"},
    ),
    LocationData(
        id = SHQ_KI_7,
        name = "Syndicate HQ: red crest 7/10",
        tags = {"Key Item"},
    ),
    LocationData(
        id = SHQ_KI_8,
        name = "Syndicate HQ: red crest 8/10",
        tags = {"Key Item"},
    ),
    LocationData(
        id = SHQ_KI_9,
        name = "Syndicate HQ: red crest 9/10",
        tags = {"Key Item"},
    ),
    LocationData(
        id = SHQ_KI_10,
        name = "Syndicate HQ: red crest 10/10",
        tags = {"Key Item"},
    ),
    LocationData(
        id = SHQ_KI_11,
        name = "Syndicate HQ: blue crest",
        tags = {"Key Item"},
    ),
    LocationData(
        id = SHQ_RCT_1,
        name = "Syndicate HQ: Radio Control Tower (Leaving)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = SHQ_RCT_2,
        name = "Syndicate HQ: Radio Control Tower (End of the World)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = SHQ_ND_1,
        name = "Syndicate HQ: Nebula Drink (Angel Ward)",
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
        id = SHQ_S_1,
        name = "Syndicate HQ: Shinji (Along the eastern face)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = SHQ_S_2,
        name = "Syndicate HQ: Shinji (Along the eastern face)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = SHQ_S_3,
        name = "Syndicate HQ: Shinji (plaza)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = SHQ_C_1,
        name = "Syndicate HQ: Carving (Damned Harmony)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = SHQ_SK_1,
        name = "Syndicate HQ: Starlight Skin (Symbols of Day Break)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = SHQ_SK_2,
        name = "Syndicate HQ: Starlight Skin (Idol Starlight)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = SHQ_SK_3,
        name = "Syndicate HQ: Starlight Skin (Bear the Shiba)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
]

SHQ_ID_TO_NAME = {
    loc.id: loc.name
    for loc in SHQ_LOCATIONS
}

SHQ_NAME_TO_ID = {
    loc.name: loc.id
    for loc in SHQ_LOCATIONS
}