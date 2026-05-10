from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in CH_LOCATIONS
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
    region: str = "Council Building"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Council Building Locations IDs
CB_IM_1  = 601

CB_KI_1  = 602

CB_RCT_1 = 603

CB_R_1   = 604
CB_R_2   = 605
CB_R_3   = 606
CB_R_4   = 607
CB_R_5   = 608

CB_S_1   = 609
CB_S_2   = 610
CB_S_3   = 611

CB_C_1   = 612

CB_SK_1  = 613
CB_SK_2  = 614
CB_SK_3  = 615
CB_SK_4  = 616

CB_WB_1  = 617



# Council Building Locations
CB_LOCATIONS = [
    LocationData(
        id = CB_IM_1,
        name = "Council Building: Island Sequence Momento 003",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = CB_KI_1,
        name = "Council Building: Customised Space Helmet",
        tags = {"Key Item"},
    ),
    LocationData(
        id = CB_RCT_1,
        name = "Council Building: Radio Control Tower (To The Heart)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = CB_R_1,
        name = "Council Building: Grotesque Pyramid Charms",
        tags = {"Relic"},
    ),
    LocationData(
        id = CB_R_2,
        name = "Council Building: Haunting Sculpture",
        tags = {"Relic"},
    ),
    LocationData(
        id = CB_R_3,
        name = "Council Building: Nauseating Offering Gems",
        tags = {"Relic"},
    ),
    LocationData(
        id = CB_R_4,
        name = "Council Building: Discarded Bottle",
        tags = {"Relic"},
    ),
    LocationData(
        id = CB_R_5,
        name = "Council Building: Lydia's Knife",
        tags = {"Relic"},
    ),
    LocationData(
        id = CB_S_1,
        name = "Council Building: Shinji (Lobby)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CB_S_2,
        name = "Council Building: Shinji (Walkway to gate)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CB_S_3,
        name = "Council Building: Shinji (Roof)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CB_C_1,
        name = "Council Building: Carving (Exclusive Slent Goat)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = CB_SK_1,
        name = "Council Building: Starlight Skin (Forbidden City)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CB_SK_2,
        name = "Council Building: Starlight Skin (Blazing Sunset)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CB_SK_3,
        name = "Council Building: Starlight Skin (Symbols of an Architect)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CB_SK_4,
        name = "Council Building: Starlight Skin (Silent Watchers)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CB_WB_1,
        name = "Council Building: Whiskey Bottle (Grinning Helper Whisky)",
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

CB_ID_TO_NAME = {
    loc.id: loc.name
    for loc in CB_LOCATIONS
}

CB_NAME_TO_ID = {
    loc.name: loc.id
    for loc in CB_LOCATIONS
}