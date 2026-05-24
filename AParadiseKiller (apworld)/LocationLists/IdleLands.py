from dataclasses import dataclass, field
from typing import Callable



def get_enabled_locations(enabled_settings: set[str]):
    return [
        loc for loc in IL_LOCATIONS
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
    region: str = "Idle Lands"

    # YAML/settings requirements
    enabled_if: Callable | None = None

    # Archipelago access rule
    rule: Callable | None = None

    # Optional categorization tags
    tags: set[str] = field(default_factory=set)



# Idle Lands Locations IDs
IL_S_1   = 101

IL_R_1   = 102
IL_R_2   = 103
IL_R_3   = 104

IL_SU_1  = 105



# Idle Lands Locations
IL_LOCATIONS = [
    LocationData(
        id = IL_S_1,
        name="Idle Lands: Shinji (bedroom)",
        tags = {"Shinji"},
    ),
    LocationData(
        id = IL_R_1,
        name="Idle Lands: Wistful Photo",
        tags = {"Relic"},
    ),
    LocationData(
        id = IL_R_2,
        name="Idle Lands: Dulled Perculator",
        tags = {"Relic"},
    ),
    LocationData(
        id = IL_R_3,
        name="Idle Lands: Well-read Book",
        tags = {"Relic"},
    ),
    LocationData(
        id = IL_SU_1,
        name="Idle Lands: Starlight Upgrade (Goat)",
        tags = {"Starlight Upgrade"},
    ),
]

IL_ID_TO_NAME = {
    loc.id: loc.name
    for loc in IL_LOCATIONS
}

IL_NAME_TO_ID = {
    loc.name: loc.id
    for loc in IL_LOCATIONS
}