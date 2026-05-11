from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in SA_LOCATIONS
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
    region: str = "Syndicate Apartments"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Syndicate Apartments Locations IDs
SA_NB_1 = 2401

SA_R_1  = 2402
SA_R_2  = 2403
SA_R_3  = 2404
SA_R_4  = 2405
SA_R_5  = 2406
SA_R_6  = 2407

SA_SK_1 = 2408



# Syndicate Apartments Locations
SA_LOCATIONS = [
    LocationData(
        id = SA_NB_1,
        name = "Syndicate Apartments: Nebula Drink (Parasol)",
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
        id = SA_R_1,
        name = "Syndicate Apartments: Maddening Rare Plant",
        tags = {"Relic"},
    ),
    LocationData(
        id = SA_R_2,
        name = "Syndicate Apartments: Aromatic Mushrooms",
        tags = {"Relic"},
    ),
    LocationData(
        id = SA_R_3,
        name = "Syndicate Apartments: Ill-Fated Pleading Letter",
        tags = {"Relic"},
    ),
    LocationData(
        id = SA_R_4,
        name = "Syndicate Apartments: Ultimate Tea",
        tags = {"Relic"},
    ),
    LocationData(
        id = SA_R_5,
        name = "Syndicate Apartments: Well Loved Secateurs",
        tags = {"Relic"},
    ),
    LocationData(
        id = SA_R_6,
        name = "Syndicate Apartments: Polite Luxury Chocolates",
        tags = {"Relic"},
    ),
    LocationData(
        id = SA_SK_1,
        name = "Syndicate Apartments: Starlight Skin (Dead Nebula)",
        enabled_if = lambda options: options.enable_starlight_skins,
        tags = {"Starlight Skin"},
    ),
]

SA_ID_TO_NAME = {
    loc.id: loc.name
    for loc in SA_LOCATIONS
}

SA_NAME_TO_ID = {
    loc.name: loc.id
    for loc in SA_LOCATIONS
}