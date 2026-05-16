from dataclasses import dataclass, field
from typing import Callable

from BaseClasses import ItemClassification



@dataclass(frozen=True)
class ItemData:
    id: int
    name: str

    # Optional metadata
    copies: int = 1
    classification: ItemClassification = ItemClassification.progression
    enabled_if: Callable | None = None
    tags: set[str] = field(default_factory=lambda: {"Key Item"})



# Key Items Items
KI_ITEMS = [
    ItemData(
        id = 1201,
        name = "Pile Bunker Gauntlets",
    ),
    ItemData(
        id = 1202,
        name = "Creased Employee Card",
    ),
    ItemData(
        id = 1203,
        name = "Glistening Stone",
    ),
    ItemData(
        id = 1204,
        name = "Crane System Unlock Card",
    ),
    ItemData(
        id = 1206,
        name = "Death Scream Device",
    ),
    
    ItemData(
        id = 1208,
        name = "Space Helmet",
    ),
    ItemData(
        id = 1209,
        name = "Lyrics",
    ),
    ItemData(
        id = 1210,
        name = "Dog Treats",
    ),
    ItemData(
        id = 1211,
        name = "Severed Arm",
    ),
    ItemData(
        id = 1212,
        name = "Corridor Key",
    ),
    ItemData(
        id = 1216,
        name = "Customised Space Helmet",
    ),
    ItemData(
        id = 1217,
        name = "Lawless Blood Dancer Eye",
    ),
]

KI_ID_TO_NAME = {
    item.id: item.name
    for item in KI_ITEMS
}

KI_NAME_TO_ID = {
    item.name: item.id
    for item in KI_ITEMS
}



