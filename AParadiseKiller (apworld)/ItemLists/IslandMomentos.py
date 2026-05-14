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
    enabled_if: Callable = lambda options: options.enable_island_momentos
    tags: set[str] = field(default_factory=lambda: {"Island Momento"})



# Island Momentos Items ID's
IM_001 = 501
IM_002 = 502
IM_003 = 503
IM_004 = 504
IM_005 = 505
IM_006 = 506
IM_007 = 507
IM_008 = 508
IM_009 = 509
IM_010 = 510
IM_011 = 511
IM_012 = 512
IM_013 = 513
IM_014 = 514
IM_015 = 515
IM_016 = 516
IM_017 = 517
IM_018 = 518
IM_019 = 519
IM_020 = 520
IM_021 = 521
IM_022 = 522
IM_023 = 523
IM_024 = 524



# Crests Items
IM_ITEMS = [
    ItemData(
        id=IM_001,
        name="Island Sequence Momento 001",
    ),
    ItemData(
        id=IM_002,
        name="Island Sequence Momento 002",
    ),
    ItemData(
        id=IM_003,
        name="Island Sequence Momento 003",
    ),
    ItemData(
        id=IM_004,
        name="Island Sequence Momento 004",
    ),
    ItemData(
        id=IM_005,
        name="Island Sequence Momento 005",
    ),
    ItemData(
        id=IM_006,
        name="Island Sequence Momento 006",
    ),
    ItemData(
        id=IM_007,
        name="Island Sequence Momento 007",
    ),
    ItemData(
        id=IM_008,
        name="Island Sequence Momento 008",
    ),
    ItemData(
        id=IM_009,
        name="Island Sequence Momento 009",
    ),
    ItemData(
        id=IM_010,
        name="Island Sequence Momento 010",
    ),
    ItemData(
        id=IM_011,
        name="Island Sequence Momento 011",
    ),
    ItemData(
        id=IM_012,
        name="Island Sequence Momento 012",
    ),
    ItemData(
        id=IM_013,
        name="Island Sequence Momento 013",
    ),
    ItemData(
        id=IM_014,
        name="Island Sequence Momento 014",
    ),
    ItemData(
        id=IM_015,
        name="Island Sequence Momento 015",
    ),
    ItemData(
        id=IM_016,
        name="Island Sequence Momento 016",
    ),
    ItemData(
        id=IM_017,
        name="Island Sequence Momento 017",
    ),
    ItemData(
        id=IM_018,
        name="Island Sequence Momento 018",
    ),
    ItemData(
        id=IM_019,
        name="Island Sequence Momento 019",
    ),
    ItemData(
        id=IM_020,
        name="Island Sequence Momento 020",
        classification = ItemClassification.progression
    ),
    ItemData(
        id=IM_021,
        name="Island Sequence Momento 021",
    ),
    ItemData(
        id=IM_022,
        name="Island Sequence Momento 022",
    ),
    ItemData(
        id=IM_023,
        name="Island Sequence Momento 023",
    ),
    ItemData(
        id=IM_024,
        name="Island Sequence Momento 024",
    ),
]

IM_ID_TO_NAME = {
    item.id: item.name
    for item in IM_ITEMS
}

IM_NAME_TO_ID = {
    item.name: item.id
    for item in IM_ITEMS
}