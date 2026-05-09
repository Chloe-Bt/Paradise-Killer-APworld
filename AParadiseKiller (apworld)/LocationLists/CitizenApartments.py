from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in CA_LOCATIONS
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
    region: str = "Citizen Apartments"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Citizen Apartments Locations IDs
CA_IM_1   = 401

CA_KI_1   = 402
CA_KI_2   = 403

CA_CR_1   = 404
CA_CR_2   = 405

CA_RCT_1  = 406
CA_RCT_2  = 407
CA_RCT_3  = 408
CA_RCT_4  = 409

CA_ND_1   = 410
CA_ND_2   = 411
CA_ND_3   = 412
CA_ND_4   = 413
CA_ND_5   = 414
CA_ND_6   = 415

CA_R_1    = 416
CA_R_2    = 417
CA_R_3    = 418
CA_R_4    = 419
CA_R_5    = 420
CA_R_6    = 421
CA_R_7    = 422
CA_R_8    = 423
CA_R_9    = 424
CA_R_10   = 425
CA_R_11   = 426
CA_R_12   = 427
CA_R_13   = 428
CA_R_14   = 429
CA_R_15   = 430
CA_R_16   = 431
CA_R_17   = 432
CA_R_18   = 433
CA_R_19   = 434
CA_R_20   = 435
CA_R_21   = 436
CA_R_22   = 437
CA_R_23   = 438
CA_R_24   = 439
CA_R_25   = 440
CA_R_26   = 441
CA_R_27   = 442

CA_S_1    = 443
CA_S_2    = 444
CA_S_3    = 445
CA_S_4    = 446
CA_S_5    = 447
CA_S_6    = 448
CA_S_7    = 449
CA_S_8    = 450
CA_S_9    = 451

CA_C_1    = 452
CA_C_2    = 453

CA_SK_1   = 454
CA_SK_2   = 455
CA_SK_3   = 456
CA_SK_4   = 457
CA_SK_5   = 458
CA_SK_6   = 459
CA_SK_7   = 460
CA_SK_8   = 461
CA_SK_9   = 462
CA_SK_10  = 463
CA_SK_11  = 464
CA_SK_12  = 465
CA_SK_13  = 466
CA_SK_14  = 467

CA_SU_1   = 468

CA_WB_1   = 469



# Citizin Apartments Locations
CA_LOCATIONS = [
    LocationData(
        id = CA_IM_1,
        name = "Citizen Apartments: Island Sequence Momento 004",
        enabled_if = lambda options: options.enable_island_momentos,
        tags = {"Island Momento"},
    ),
    LocationData(
        id = CA_KI_1,
        name = "Citizen Apartments: Imperfect Dominoes",
        tags = {"Key Item"},
    ),
    LocationData(
        id = CA_KI_2,
        name = "Citizen Apartments: Glistening Stone",
        tags = {"Key Item"},
    ),
    LocationData(
        id = CA_CR_1,
        name = "Citizen Apartments: Green Crest (Rooftop)",
        tags = {"Key Item"},
    ),
    LocationData(
        id = CA_CR_2,
        name = "Citizen Apartments: Green Crest (Narrow Alley)",
        tags = {"Key Item"},
    ),
    LocationData(
        id = CA_RCT_1,
        name = "Citizen Apartments: Radio Control Tower (Lady Blue)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = CA_RCT_2,
        name = "Citizen Apartments: Radio Control Tower (Sunset Song)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = CA_RCT_3,
        name = "Citizen Apartments: Radio Control Tower (Last Dance XX)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = CA_RCT_4,
        name = "Citizen Apartments: Radio Control Tower (Ego 24-7)",
        enabled_if = lambda options: options.enable_music_tracks,
        tags = {"Radio Control Tower"},
    ),
    LocationData(
        id = CA_ND_1,
        name = "Citizen Apartments: Nubula Drink (Cool Melon)",
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
        id = CA_ND_2,
        name = "Citizen Apartments: Nubula Drink (Acid's Favorite)",
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
        id = CA_ND_3,
        name = "Citizen Apartments: Nubula Drink (Lost Mountain Water)",
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
        id = CA_ND_4,
        name = "Citizen Apartments: Nubula Drink (Water)",
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
        id = CA_ND_5,
        name = "Citizen Apartments: Nubula Drink (Evening Haze)",
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
        id = CA_ND_6,
        name = "Citizen Apartments: Nubula Drink (Kill The Thirst)",
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
        id = CA_R_1,
        name = "Citizen Apartments: Grubby Skimming Runes",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_2,
        name = "Citizen Apartments: Glinting Golden Crown",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_3,
        name = "Citizen Apartments: Gaudy Blood Pendant",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_4,
        name = "Citizen Apartments: Suspicious Video Tape",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_5,
        name = "Citizen Apartments: Cheerful Children's Book",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_6,
        name = "Citizen Apartments: Fancy Playing Cards",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_7,
        name = "Citizen Apartments: Dazzling Obelisk",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_8,
        name = "Citizen Apartments: Absurd Message Stones",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_9,
        name = "Citizen Apartments: Malicious Secretive Cassette",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_10,
        name = "Citizen Apartments: Ill-fated Ring Pulls",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_11,
        name = "Citizen Apartments: Righteous Monserrat T-Shirt",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_12,
        name = "Citizen Apartments: Enchanting Blood Charm",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_13,
        name = "Citizen Apartments: Incoherent Abandoned Diary",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_14,
        name = "Citizen Apartments: Lurid Crimson Acid Phone Charm",
        tags = {"Relic"},
    ),
    LocationData(
        id =CA_R_15 ,
        name = "Citizen Apartments: Questionable Donation",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_16,
        name = "Citizen Apartments: Resonant Photo of a Man",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_17,
        name = "Citizen Apartments: Wonderful Crystallized Tears",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_18,
        name = "Citizen Apartments: Nostalgic Fallen Rose",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_19,
        name = "Citizen Apartments: Abnormal Butterfly",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_20,
        name = "Citizen Apartments: Polished Badge",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_21,
        name = "Citizen Apartments: Wistful Lovers Padlock",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_22,
        name = "Citizen Apartments: Recondite Ornate Book",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_23,
        name = "Citizen Apartments: Knowledgeable Listening Device",
        tags = {"Relic"},
    ),
    LocationData(
        id =CA_R_24 ,
        name = "Citizen Apartments: Tawdry Poster",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_25,
        name = "Citizen Apartments: Dazzling Obelisk Charm",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_26,
        name = "Citizen Apartments: Descriptive River Power Station Schedule",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_R_27,
        name = "Citizen Apartments: Fascinating Grasshopper",
        tags = {"Relic"},
    ),
    LocationData(
        id = CA_S_1,
        name = "Citizen Apartments: Shinji (sewer entrance)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CA_S_2,
        name = "Citizen Apartments: Shinji (rooftop Silent Goat Apartments)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CA_S_3,
        name = "Citizen Apartments: Shinji (pool Silent Goat Apartment)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CA_S_4,
        name = "Citizen Apartments: Shinji (ground floor Lost Love Residential)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CA_S_5,
        name = "Citizen Apartments: Shinji (thin metal tower)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CA_S_6,
        name = "Citizen Apartments: Shinji (rooftop Another Dusk Apartment)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CA_S_7,
        name = "Citizen Apartments: Shinji (storage shed Another Dusk Apartment)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CA_S_8,
        name = "Citizen Apartments: Shinji (rooftop Poisoned Throne Apartments)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CA_S_9,
        name = "Citizen Apartments: Shinji (stairwell Dreaded Hero Apartments)",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = CA_C_1,
        name = "Citizen Apartments: Carving (Enchanted Blue)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = CA_C_2,
        name = "Citizen Apartments: Carving (Silent Goat)",
        enabled_if = lambda options: options.enable_shrines,
        tags = {"Carving"},
    ),
    LocationData(
        id = CA_SK_1,
        name = "Citizen Apartments: Starlight Skin (Symbol of the Secretary)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_2,
        name = "Citizen Apartments: Starlight Skin (Verdant)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_3,
        name = "Citizen Apartments: Starlight Skin (Warmth of the Moon)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_4,
        name = "Citizen Apartments: Starlight Skin (Symbols of the Possessed)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_5,
        name = "Citizen Apartments: Starlight Skin (Creeping Flora)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_6,
        name = "Citizen Apartments: Starlight Skin (Incomprehensible Starlight)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_7,
        name = "Citizen Apartments: Starlight Skin (Inscribed in the Surface)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_8,
        name = "Citizen Apartments: Starlight Skin (Investigation Freak)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_9,
        name = "Citizen Apartments: Starlight Skin (Glimpse of Serenity)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_10,
        name = "Citizen Apartments: Starlight Skin (Impassable Space)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_11,
        name = "Citizen Apartments: Starlight Skin (Possible Crucible)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_12,
        name = "Citizen Apartments: Starlight Skin (A Billion Stars)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_13,
        name = "Citizen Apartments: Starlight Skin (Fleeing Moon)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SK_14,
        name = "Citizen Apartments: Starlight Skin (Pop Art)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = CA_SU_1,
        name = "Citizen Apartments: Starlight Upgrade (Cosmos)",
        tags = {"Starlight Upgrade"},
    ),
    LocationData(
        id = CA_WB_1,
        name = "Citizen Apartments: Whisky Bottle (No Reality Whisky)",
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

CA_ID_TO_NAME = {
    loc.id: loc.name
    for loc in CA_LOCATIONS
}

CA_NAME_TO_ID = {
    loc.name: loc.id
    for loc in CA_LOCATIONS
}