#Reality Folding Drive
RFD_ID_TO_NAME = {}
ALL_RFD = list(RFD_ID_TO_NAME.keys())

from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in RFD_LOCATIONS
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
    region: str = "Reality Folding Drive"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Reality Folding Drive Locations IDs
RFD_Q_1   = 2101

RFD_IM_1  = 2102

RFD_KI_1  = 2103

#RFD_RCT_1 = 2104

RFD_ND_1  = 2105
RFD_ND_2  = 2106

RFD_S_1   = 2107
RFD_S_2   = 2108

RFD_SK_1  = 2109
RFD_SK_2  = 2110
RFD_SK_3  = 2111

RFD_SU_1  = 2112

RFD_WB_1  = 2113

# Reality Folding Drive Locations
RFD_LOCATIONS = [
    LocationData(
        id = RFD_Q_1,
        name = "Reality Folding Drive: Complete Ghost Quest (Wayward Ghost)",
        rule = lambda state, options, player: state.has("Creased Employee Card", player),
        tags = {"Quest"},
    ),
    LocationData(
        id = RFD_IM_1,
        name = "Reality Folding Drive: Island Sequence Momento 011",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = RFD_KI_1,
        name = "Reality Folding Drive: Lyrics",
        tags = {"Key Item"},
    ),
    LocationData(
        id = RFD_ND_1,
        name = "Reality Folding Drive: Nebula Drink (Provocative Flower)",
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
        id = RFD_ND_2,
        name = "Reality Folding Drive: Deader Nebula",
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
        id = RFD_S_1,
        name = "Reality Folding Drive: Shinji (Under concrete bridge)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = RFD_S_2,
        name = "Reality Folding Drive: Shinji (on roof RFD)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            (not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player))
            and state.has("LLD Upgrade: Double Jump", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = RFD_SK_1,
        name = "Reality Folding Drive: Starlight Skin (Symbols of the Witness)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = RFD_SK_2,
        name = "Reality Folding Drive: Starlight Skin (Symbol of a Bar Master)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = RFD_SK_3,
        name = "Reality Folding Drive: Starlight Skin (Transmission Tower)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = RFD_SU_1,
        name = "Reality Folding Drive: Starlight Upgrade (Pyramids)",
        rule = lambda state, options, player: state.has("Locker Code", player),
        tags = {"Starlight Upgrade"},
    ),
    LocationData(
        id = RFD_WB_1,
        name = "Reality Folding Drive: Whisky Bottle (Mikami's Masterpiece 4 Whisky)",
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

RFD_ID_TO_NAME = {
    loc.id: loc.name
    for loc in RFD_LOCATIONS
}

RFD_NAME_TO_ID = {
    loc.name: loc.id
    for loc in RFD_LOCATIONS
}