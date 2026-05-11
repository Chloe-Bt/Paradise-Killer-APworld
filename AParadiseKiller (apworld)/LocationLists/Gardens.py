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



# Garden Locations IDs
G_Q_1  = 1301
G_Q_2  = 1302

G_ND_1 = 1303

G_R_1  = 1304
G_R_2  = 1305
G_R_3  = 1306

G_S_1  = 1307

G_SK_1 = 1308
G_SK_2 = 1309


# Garden Locations
G_LOCATIONS = [
    LocationData(
        id = G_Q_1,
        name = "Garden: Finish Ghost Quest (Searching Ghost)",
        rule = lambda state, options, player: state.has("Vampire Report", player),
        tags = {"Quest"},
    ),
    LocationData(
        id = G_Q_2,
        name = "Garden: Finish Ghost Quest (Anarchic Ghost)",
        rule = lambda state, options, player: state.has("Glistening Stone", player),
        tags = {"Quest"},
    ),
    LocationData(
        id = G_ND_1,
        name = "Garden: Nebula Drink (Indefinable Spectrum)",
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
        id = G_R_1,
        name = "Garden: Vapid Book",
        tags = {"Relic"},
    ),
    LocationData(
        id = G_R_2,
        name = "Garden: Fantastic Crystallized Tear Necklace",
        tags = {"Relic"},
    ),
    LocationData(
        id = G_R_3,
        name = "Garden: Splendid Pamphlet",
        tags = {"Relic"},
    ),
    LocationData(
        id = G_S_1,
        name = "Garden: Shinji",
        enabled_if = lambda options: options.enable_shinji_locations,
        rule = lambda state, options, player: (
            not options.enable_demon_translator
            or state.has("Demon Translator (unlocks Shinji locations)", player)
        ),
        tags = {"Shinji"},
    ),
    LocationData(
        id = G_SK_1,
        name = "Garden: Starlight Skin (Symbols of a Warrior)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
    LocationData(
        id = G_SK_2,
        name = "Garden: Starlight Skin (Final Moments)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
]

G_ID_TO_NAME = {
    loc.id: loc.name
    for loc in G_LOCATIONS
}

G_NAME_TO_ID = {
    loc.name: loc.id
    for loc in G_LOCATIONS
}