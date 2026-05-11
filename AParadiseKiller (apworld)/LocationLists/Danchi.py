from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in D_LOCATIONS
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
    region: str = "Danchi"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Danchi Locations IDs
D_Q_1    = 801

D_KI_1   = 802
D_KI_2   = 803
D_KI_3   = 804
D_KI_4   = 805

D_RCT_1  = 806
D_RCT_2  = 807

D_ND_1   = 808
D_ND_2   = 809
D_ND_3   = 810
D_ND_4   = 811

D_R_1    = 812
D_R_2    = 813
D_R_3    = 814
D_R_4    = 815
D_R_5    = 816
D_R_6    = 817
D_R_7    = 818
D_R_8    = 819
D_R_9    = 820
D_R_10   = 821

D_S_1    = 822
D_S_2    = 823
D_S_3    = 824
D_S_4    = 825
D_S_5    = 826
D_S_6    = 827
D_S_7    = 828

D_C_1    = 829

D_SK_1   = 830
D_SK_2   = 831
D_SK_3   = 832
D_SK_4   = 833
D_SK_5   = 834
D_SK_6   = 835

D_WB_1   = 836



# Danchi Locations
D_LOCATIONS = [
    LocationData(
        id = D_Q_1,
        name = "Danchi: Finish Ghost Quest - Grieving Ghost",
        rule = lambda state, options, player: state.has("Severed Arm", player),
        tags = {"Quest"},
    ),
    LocationData(
        id = D_KI_1,
        name = "Danchi: Severed Hand",
        tags = {"Key Item"},
    ),
    LocationData(
        id = D_KI_2,
        name = "Danchi: Severed Arm",
        tags = {"Key Item"},
    ),
    LocationData(
        id = D_KI_3,
        name = "Danchi: Yellow Crest (Danchi tower)",
        tags = {"Key Item"},
    ),
    LocationData(
        id = D_KI_4,
        name = "Danchi: Yellow Crest (walkway)",
        tags = {"Key Item"},
    ),
    LocationData(
        id = D_RCT_1,
        name = "Danchi: Radio Control Tower (The Lemegeton Bop)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = D_RCT_2,
        name = "Danchi: Radio Control Tower (Unlimited∞Luv)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = D_ND_1,
        name = "Danchi: Nebula Drink (Parallel Red)",
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
        id = D_ND_2,
        name = "Danchi: Nebula Drink (Aesthestic Water)",
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
        id = D_ND_3,
        name = "Danchi: Nebula Drink (Tropical Demolition)",
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
        id = D_ND_4,
        name = "Danchi: Devil Nebula",
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
        id = D_R_1,
        name = "Danchi: Desirable Bear Chan Phone Charm",
        tags = {"Relic"},
    ),
    LocationData(
        id = D_R_2,
        name = "Danchi: Inquisitive Apartment Murder Report",
        tags = {"Relic"},
    ),
    LocationData(
        id = D_R_3,
        name = "Danchi: Efficacious Chillies",
        tags = {"Relic"},
    ),
    LocationData(
        id = D_R_4,
        name = "Danchi: Discarded Pistachios",
        tags = {"Relic"},
    ),
    LocationData(
        id = D_R_5,
        name = "Danchi: Gleaming Male Idol Card",
        tags = {"Relic"},
    ),
    LocationData(
        id = D_R_6,
        name = "Danchi: Extrinsic Fossil",
        tags = {"Relic"},
    ),
    LocationData(
        id = D_R_7,
        name = "Danchi: Contemplative Painting",
        tags = {"Relic"},
    ),
    LocationData(
        id = D_R_8,
        name = "Danchi: Cute Tamago Phone Charm",
        tags = {"Relic"},
    ),
    LocationData(
        id = D_R_9,
        name = "Danchi: Tremendous Game Cart",
        tags = {"Relic"},
    ),
    LocationData(
        id = D_R_10,
        name = "Danchi: Joyous Fish Food",
        tags = {"Relic"},
    ),
    LocationData(
        id = D_S_1,
        name = "Danchi: Shinji (northwestern corner)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = D_S_2,
        name = "Danchi: Shinji (southwestern corner)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = D_S_3,
        name = "Danchi: Shinji (5th floor)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = D_S_4,
        name = "Danchi: Shinji (rooftop)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = D_S_5,
        name = "Danchi: Shinji (northeastern corner)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = D_S_6,
        name = "Danchi: Shinji (Below walkway)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = D_S_7,
        name = "Danchi: Shinji (under seawall walkway)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = D_C_1,
        name = "Danchi: Carving (Crying Grudge)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = D_SK_1,
        name = "Danchi: Starlight Skin (Grim Lotus)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = D_SK_2,
        name = "Danchi: Starlight Skin (Beautiful Blossom)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = D_SK_3,
        name = "Danchi: Starlight Skin (Bathed Towers)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = D_SK_4,
        name = "Danchi: Starlight Skin (Dimensional Breakdown)",
        enabled_if = lambda options: options.enable_starlight_skins,
        rule = lambda state, options, player: (
            state.has("Imperfect Dominoes", player),
            state.has("Island Sequence Momento - 020", player),
            state.has("Music Track - Go! Go! Style", player),
        ),
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = D_SK_5,
        name = "Danchi: Starlight Skin (Ancient Battlefield)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = D_SK_6,
        name = "Danchi: Starlight Skin (Symbol of a Kiss)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = D_WB_1,
        name = "Danchi: Whisky Bottle (Evening Melancholy Whisky)",
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

D_ID_TO_NAME = {
    loc.id: loc.name
    for loc in D_LOCATIONS
}

D_NAME_TO_ID = {
    loc.name: loc.id
    for loc in D_LOCATIONS
}