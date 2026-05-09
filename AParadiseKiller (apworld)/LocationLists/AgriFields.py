from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in AF_LOCATIONS
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
    region: str = "Agri Fields"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Agri Fields Locations IDs
AF_IM_1  = 201

AF_KI_1  = 202
AF_KI_2  = 203
AF_KI_3  = 204
AF_KI_4  = 205

AF_RCT_1 = 206
AF_ND_1  = 207

AF_Q_1   = 208
AF_Q_2   = 209

AF_RC_1  = 210

AF_R_1   = 211
AF_R_2   = 212

AF_S_1   = 213
AF_S_2   = 214

AF_SK_1  = 215
AF_SK_2  = 216
AF_SK_3  = 217

AF_WB_1  = 218



# Agri Fields Locations
AF_LOCATIONS = [
    #Island Momentos
    LocationData(
        id = AF_IM_1,
        name="Agri Fields: Island Sequence Momento 010",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),

    # Key Items
    LocationData(
        id = AF_KI_1,
        name="Agri Fields: Protest Letter",
        tags = {"Key Item"},
    ),
    LocationData(
        id = AF_KI_2,
        name="Agri Fields: Valve Handle 1",
        tags = {"Key Item"},
    ),
    LocationData(
        id = AF_KI_3,
        name="Agri Fields: Valve Handle 2",
        tags = {"Key Item"},
    ),
    LocationData(
        id = AF_KI_4,
        name="Agri Fields: Valve Handle 3",
        tags = {"Key Item"},
    ),

    # Radio Control Tower
    LocationData(
        id = AF_RCT_1,
        name="Agri Fields: Radio Control Tower (Go! Go! Style)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),

    # Nebula Drink
    LocationData(
        id = AF_ND_1,
        name="Agri Fields: Nebula Drink (Bizarre Lychee)",
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

    #Recording
    LocationData(
        id = AF_RC_1,
        name="Agri Fields: Recording 004",
        enabled_if = lambda options: options.enable_recordings,
        tags = {"Recording"},
    ),

    #Whisky Bottle
    LocationData(
        id = AF_WB_1,
        name="Agri Fields: Whisky Bottle (Seven Spies Whisky)",
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

    # Quests
    LocationData(
        id = AF_Q_1,
        name="Agri Fields: Watering the Agri Fields",
        tags = {"Quest"},
    ),
    LocationData(
        id = AF_Q_2,
        name="Agri Fields: Activate the Comms Tower",
        tags = {"Quest"},
    ),
    
    # Relics
    LocationData(
        id = AF_R_1,
        name="Agri Fields: Covetable Workers Reward",
        tags = {"Relic"},
    ),

    LocationData(
        id = AF_R_2,
        name="Agri Fields: Proud Pin Badge",
        tags = {"Relic"},
    ),

    # Shinji
    LocationData(
        id = AF_S_1,
        name="Agri Fields: Shinji (crop patch)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = AF_S_2,
        name="Agri Fields: Shinji (comms tower)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    
    # Starlight Skins
    LocationData(
        id = AF_SK_1,
        name="Agri Fields: Starlight Skin (Loquacious Jellyfish)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = AF_SK_2,
        name="Agri Fields: Starlight Skin (Fortified Desert)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = AF_SK_3,
        name="Agri Fields: Starlight Skin (Wonderful Skyline)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
]

AF_ID_TO_NAME = {
    loc.id: loc.name
    for loc in AF_LOCATIONS
}

AF_NAME_TO_ID = {
    loc.name: loc.id
    for loc in AF_LOCATIONS
}