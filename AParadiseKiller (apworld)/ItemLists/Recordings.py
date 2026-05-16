from dataclasses import dataclass, field
from typing import Callable

from BaseClasses import ItemClassification


@dataclass(frozen=True)
class ItemData:
    id: int
    name: str

    # Optional metadata
    copies: int = 1
    classification: ItemClassification = ItemClassification.filler
    enabled_if: Callable = lambda options: options.enable_recordings
    tags: set[str] = field(default_factory=lambda: {"Recording"})


# Recordings Items ID's
REC_001 = 801
REC_002 = 802
REC_003 = 803
REC_004 = 804
REC_005 = 805
REC_013 = 806



# Recordings Items
RECORDING_ITEMS = [
    ItemData(
        id=REC_001,
        name="Recording 001",
    ),
    ItemData(
        id=REC_002,
        name="Recording 002",
    ),
    ItemData(
        id=REC_003,
        name="Recording 003",
    ),
    ItemData(
        id=REC_004,
        name="Recording 004",
    ),
    ItemData(
        id=REC_005,
        name="Recording 005",
    ),
    ItemData(
        id=REC_013,
        name="Recording 013",
    ),
]

RECORDING_ID_TO_NAME = {
    item.id: item.name
    for item in RECORDING_ITEMS
}

RECORDING_NAME_TO_ID = {
    item.name: item.id
    for item in RECORDING_ITEMS
}
