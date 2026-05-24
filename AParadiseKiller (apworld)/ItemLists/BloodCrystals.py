from dataclasses import dataclass, field
from typing import Callable

from BaseClasses import ItemClassification





@dataclass(frozen=True)
class ItemData:
    id: int
    name: str

    # Optional metadata
    copies: int = 1
    classification: ItemClassification = ItemClassification.useful
    enabled_if: Callable | None = None
    tags: set[str] = field(default_factory=lambda: {"Blood Crystal"})



# Blood Crystal Items ID's
BC_0   = 1000



# Blood Crystal Items
BC_ITEMS = [
    ItemData(
        id = 1000,
        name = "Blood Crysal",
        copies = 4,
        classification = ItemClassification.filler,
    ),
]

BC_ID_TO_NAME = {
    item.id: item.name
    for item in BC_ITEMS
}

BC_NAME_TO_ID = {
    item.name: item.id
    for item in BC_ITEMS
}


