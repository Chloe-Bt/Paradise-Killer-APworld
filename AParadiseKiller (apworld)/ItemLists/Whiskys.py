from dataclasses import dataclass, field
from typing import Callable

from BaseClasses import ItemClassification



@dataclass(frozen=True)
class ItemData:
    id: int
    name: str

    # Optional metadata
    copies: int = 1
    classification: Callable = lambda options: (
        ItemClassification.progression
        if options.goal == "lady_whisky_dies"
        else ItemClassification.filler
    )
    enabled_if: Callable = lambda options: (
        options.enable_whisky_bottles
        or options.goal == "lady_whisky_dies"
    )
    tags: set[str] = field(default_factory=lambda: {"Whisky Bottle"})



# Whisky Bottles Items ID's
WHISKY_HAIR         = 201
WHISKY_GRINNING     = 202
WHISKY_NOR          = 203
WHISKY_AN           = 204
WHISKY_CHAOS        = 205
WHISKY_GOTHIC       = 206
WHISKY_WINNING      = 207
WHISKY_EVENING      = 208
WHISKY_CODE         = 209
WHISKY_DEAD         = 210
WHISKY_NOW          = 211
WHISKY_SEVEN        = 212
WHISKY_MIKAMIS      = 213



# Whisky Bottles Items
WHISKY_ITEMS = [
    ItemData(WHISKY_HAIR, "Hair Trigger Whisky"),
    ItemData(WHISKY_GRINNING, "Grinning Helper Whisky"),
    ItemData(WHISKY_NOR, "No Reality Whisky"),
    ItemData(WHISKY_AN, "An Answer Lost Whisky"),
    ItemData(WHISKY_CHAOS, "Chaos Domain Whisky"),
    ItemData(WHISKY_GOTHIC, "A Gothic Second Whisky"),
    ItemData(WHISKY_WINNING, "Winning Devil Whisky"),
    ItemData(WHISKY_EVENING, "Evening Melancholy Whisky"),
    ItemData(WHISKY_CODE, "Code Whisky"),
    ItemData(WHISKY_DEAD, "Dead Man's Ambitious Whisky"),
    ItemData(WHISKY_NOW, "No Warning Whisky"),
    ItemData(WHISKY_SEVEN, "Seven Spies Whisky"),
    ItemData(WHISKY_MIKAMIS, "Mikami's Masterpiece 4 Whisky"),
]

WHISKY_ID_TO_NAME = {
    item.id: item.name
    for item in WHISKY_ITEMS
}

WHISKY_NAME_TO_ID = {
    item.name: item.id
    for item in WHISKY_ITEMS
}
