from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in B_LOCATIONS
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
    region: str = "Beach"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Agri Fields Locations IDs
B_Q_1   = 301
B_Q_4   = 304

B_IM_1  = 305

B_RDC_1 = 306

B_ND_1  = 307
B_ND_2  = 308

B_RC_1  = 309

B_R_1   = 310
B_R_2   = 311

B_S_1   = 312
B_S_2   = 313

B_C_1   = 314

B_SK_1  = 315
B_SK_2  = 316
B_SK_3  = 317
B_SK_4  = 318

B_WB_1  = 319



# Beach Locations
B_LOCATIONS = [
    LocationData(
        id = B_Q_1,
        name="Beach: Complete Ghost Quest (Horrified Ghost)",
        rule = lambda state, options, player: (
            state.has("Vampire Report", player)
        ),
        tags = {"Quest"},
    ),
    LocationData(
        id = B_Q_4,
        name="Beach: Activate Obelish Control Panel",
        tags = {"Quest"},
    ),
    LocationData(
        id = B_IM_1,
        name="Beach: Island Sequence Momento 019",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = B_RDC_1,
        name="Beach: Radio Control Tower (Headlights on the Shore)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = B_ND_1,
        name="Beach: Nubula Drink (Pillar Flower)",
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
        id = B_ND_2,
        name="Beach: Nebula Drink (Power of Goat Soda)",
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
        id = B_RC_1,
        name="Beach: Recording 005",
        enabled_if = lambda options: options.enable_recordings,
        tags = {"Recording"},
    ),
    LocationData(
        id = B_R_1,
        name="Beach: Quivering Jellyfish",
        tags = {"Relic"},
    ),
    LocationData(
        id = B_R_2,
        name="Beach: Playful Stones",
        tags = {"Relic"},
    ),
    LocationData(
        id = B_S_1,
        name="Beach: Shinji (beach)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = B_S_2,
        name="Beach: Shinji (up on the cliffs)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = B_C_1,
        name="Beach: Carving (Lost Pain)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = B_SK_1,
        name="Beach: Starlight Skin (Aspirational View)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = B_SK_2,
        name="Beach: Starlight Skin (Ancient Text)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = B_SK_3,
        name="Beach: Starlight Skin (Tropical Starlight)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = B_SK_4,
        name="Beach: Starlight Skin (End of Day)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = B_WB_1,
        name="Beach: Whisky Bottle (Code Whisky)",
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
B_ID_TO_NAME = {
    loc.id: loc.name
    for loc in B_LOCATIONS
}

B_NAME_TO_ID = {
    loc.name: loc.id
    for loc in B_LOCATIONS
}