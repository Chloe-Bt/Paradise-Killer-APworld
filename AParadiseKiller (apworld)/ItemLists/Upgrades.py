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
    tags: set[str] = field(default_factory=lambda: {"Upgrades"})



# Upgrades Items IDs
SU_GOAT     = 401
SU_COSMOS   = 402
SU_WORSHIP  = 403
SU_PYRAMIDS = 404
FB_MEDITATE = 405
FB_DASH     = 406
FB_DJUMP    = 407


# Upgrades Items
UPGRADE_ITEMS = [
    ItemData(SU_GOAT, "Starlight Upgrade: Goat"),
    ItemData(SU_COSMOS, "Starlight Upgrade: Cosmos"),
    ItemData(SU_WORSHIP, "Starlight Upgrade: Worship"),
    ItemData(SU_PYRAMIDS, "Starlight Upgrade: Pyramids"),
    ItemData(FB_MEDITATE, "LLD Upgrade: Meditate"),
    ItemData(FB_DASH, "LLD Upgrade: Air Dash"),
    ItemData(FB_DJUMP, "LLD Upgrade: Double Jump"),
]

UPGRADE_ID_TO_NAME = {
    item.id: item.name
    for item in UPGRADE_ITEMS
}

UPGRADE_NAME_TO_ID = {
    item.name: item.id
    for item in UPGRADE_ITEMS
}
