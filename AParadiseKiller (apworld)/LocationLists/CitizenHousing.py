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
    region: str = "Citizen Housing"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)




# Citizen Housing Locations IDs
CH_IM_1  = 501
CH_IM_2  = 502
CH_IM_3  = 503
CH_IM_4  = 504
CH_IM_5  = 505
CH_IM_6  = 506
CH_IM_7  = 507

CH_CR_1  = 508
CH_CR_2  = 509

CH_KI_1  = 510
CH_KI_2  = 511
CH_KI_3  = 512
#CH_KI_4  = 513
#CH_KI_5  = 514

CH_RCT_1 = 515
CH_RCT_2 = 516

CH_ND_1  = 517
CH_ND_2  = 518
CH_ND_3  = 519

CH_Q_1   = 520

CH_R_1   = 521
CH_R_2   = 522
CH_R_3   = 523
CH_R_4   = 524
CH_R_5   = 525
CH_R_6   = 526
CH_R_7   = 527
CH_R_8   = 528
CH_R_9   = 529
CH_R_10  = 530

CH_S_1   = 531
CH_S_2   = 532
CH_S_3   = 533
CH_S_4   = 534
CH_S_5   = 535
#CH_S_6   = 536 wrong count?
#CH_S_7   = 537 wrong count?

CH_C_1   = 538
CH_C_2   = 539

CH_SK_1  = 540
CH_SK_2  = 541
CH_SK_3  = 542
CH_SK_4  = 543
CH_SK_5  = 544
CH_SK_6  = 545

CH_WB_1  = 546
CH_WB_2  = 547
CH_WB_3  = 548



# Citizen Housing Locations
CH_LOCATIONS = [
    LocationData(
        id = CH_IM_1,
        name = "Citizen Housing: Island Sequence Momento 005",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = CH_IM_2,
        name = "Citizen Housing: Island Sequence Momento 006",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = CH_IM_3,
        name = "Citizen Housing: Island Sequence Momento 015",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = CH_IM_4,
        name = "Citizen Housing: Island Sequence Momento 018",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = CH_IM_5,
        name = "Citizen Housing: Island Sequence Momento 022",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = CH_IM_6,
        name = "Citizen Housing: Island Sequence Momento 023",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = CH_IM_7,
        name = "Citizen Housing: Island Sequence Momento 024",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = CH_CR_1,
        name = "Citizen Housing: Blue Crest (Behind Convenience Store)",
        tags = {"Key Item"},
    ),
    LocationData(
        id = CH_CR_2,
        name = "Citizen Housing: Blue Crest (In River)",
        tags = {"Key Item"},
    ),
    LocationData(
        id = CH_KI_1,
        name = "Citizen Housing: Dog Treats",
        tags = {"Key Item"},
    ),
    LocationData(
        id = CH_KI_2,
        name = "Citizen Housing: Creased Employee Card",
        tags = {"Key Item"},
    ),
    LocationData(
        id = CH_KI_3,
        name = "Citizen Housing: Pile Bunker Gauntlets",
        tags = {"Key Item"},
    ),
    LocationData(
        id = CH_RCT_1,
        name = "Citizen Housing: Radio Control Tower (8th Street Rose)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = CH_RCT_2,
        name = "Citizen Housing: Radio Control Tower (House of Bliss)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = CH_ND_1,
        name = "Citizen Housing: Nebula Drink (Sanitea)",
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
        id = CH_ND_2,
        name = "Citizen Housing: Nebula Drink (Crystal Sparkling Water)",
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
        id = CH_ND_3,
        name = "Citizen Housing: Nebula Drink (O.O.O.)",
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
        id = CH_Q_1,
        name = "Citizen Housing: Give Dog Treats to Bear",
        rule = lambda state, options, player: state.has("Dog Treats", player),
        tags = {"Quest"},
    ),
    LocationData(
        id = CH_R_1,
        name = "Citizen Housing: Inaccurate Alarm Clock",
        tags = {"Relic"},
    ),
    LocationData(
        id = CH_R_2,
        name = "Citizen Housing: Coveted Loyalty Card",
        tags = {"Relic"},
    ),
    LocationData(
        id =CH_R_3 ,
        name = "Citizen Housing: Obsequious Love Letter",
        tags = {"Relic"},
    ),
    LocationData(
        id = CH_R_4,
        name = "Citizen Housing: Duplicated Rotten Eggs",
        tags = {"Relic"},
    ),
    LocationData(
        id =CH_R_5 ,
        name = "Citizen Housing: Fashionable Dead Nebula Phone Charm",
        tags = {"Relic"},
    ),
    LocationData(
        id = CH_R_6,
        name = "Citizen Housing: Idiotic Loyalty Levels",
        tags = {"Relic"},
    ),
    LocationData(
        id = CH_R_7,
        name = "Citizen Housing: Wretched CD",
        tags = {"Relic"},
    ),
    LocationData(
        id = CH_R_8,
        name = "Citizen Housing: Unavoidable Pain Pills",
        tags = {"Relic"},
    ),
    LocationData(
        id = CH_R_9,
        name = "Citizen Housing: Glittering Sequin Ward",
        tags = {"Relic"},
    ),
    LocationData(
        id = CH_R_10,
        name = "Citizen Housing: Shameful Fake Golden Crown",
        tags = {"Relic"},
    ),
    LocationData(
        id = CH_S_1,
        name = "Citizen Housing: Shinji (river behind park)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CH_S_2,
        name = "Citizen Housing: Shinji (two-storey apartment leading to Mountain Gorge)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CH_S_3,
        name = "Citizen Housing: Shinji (ladders atop deep factory)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CH_S_4,
        name = "Citizen Housing: Shinji (Atop a house oposite of Dead Zone)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CH_S_5,
        name = "Citizen Housing: Shinji (Leading to Dead Zone)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CH_C_1,
        name = "Citizen Housing: Carving (Endless Moon)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = CH_C_2,
        name = "Citizen Housing: Carving (Nighhtmare Revival)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = CH_SK_1,
        name = "Citizen Housing: Starlight Skin (Blissful Sky)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CH_SK_2,
        name = "Citizen Housing: Starlight Skin (Vibing)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CH_SK_3,
        name = "Citizen Housing: Starlight Skin (Mysterious Carp)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CH_SK_4,
        name = "Citizen Housing: Starlight Skin (Hallowed Bamboo)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CH_SK_5,
        name = "Citizen Housing: Starlight Skin (Escape to the City)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CH_SK_6,
        name = "Citizen Housing: Starlight Skin (The Day Breaks)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CH_WB_1,
        name = "Citizen Housing: Whisky Bottle (An Answer Lost Whisky)",
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
    LocationData(
        id = CH_WB_2,
        name = "Citizen Housing: Whisky Bottle (Chaos Domain Whisky)",
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
    LocationData(
        id = CH_WB_3,
        name = "Citizen Housing: Whisky Bottle (A Gothic Second Whisky)",
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

CH_ID_TO_NAME = {
    loc.id: loc.name
    for loc in CH_LOCATIONS
}

CH_NAME_TO_ID = {
    loc.name: loc.id
    for loc in CH_LOCATIONS
}