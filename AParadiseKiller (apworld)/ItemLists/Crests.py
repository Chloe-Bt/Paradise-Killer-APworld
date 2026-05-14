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
    tags: set[str] = field(default_factory=lambda: {"Crests"})



# Crests Items ID's
CREST_BLUE   = 601
CREST_YELLOW = 602
CREST_GREEN  = 603
CREST_RED    = 604
VALVE        = 605

# Crests Items
CREST_ITEMS = [
    ItemData(
        id=CREST_BLUE,
        name="Blue Crest",
        copies = 2,
    ),
    ItemData(
        id=CREST_YELLOW,
        name="Yellow Crest",
        copies = 2,
    ),
    ItemData(
        id=CREST_GREEN,
        name="Green Crest",
        copies = 2,
    ),
    ItemData(
        id=CREST_RED,
        name="Red Crest",
        copies = 10,
    ),
    ItemData(
        id=VALVE,
        name="Valve Handle",
        copies = 3,
    ),
]

CREST_ID_TO_NAME = {
    item.id: item.name
    for item in CREST_ITEMS
}

CREST_NAME_TO_ID = {
    item.name: item.id
    for item in CREST_ITEMS
}



