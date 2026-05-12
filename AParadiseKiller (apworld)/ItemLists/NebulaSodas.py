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
    enabled_if: Callable = lambda options: (
        options.enable_nebula_drinks
        or options.goal == "lady_soda_dies"
    )
    tags: set[str] = field(default_factory=lambda: {"Nebula Drink"})



# Nebula Soda Items
SODA_ITEMS = [
    ItemData(101, "Nebula Drink: Angel Ward"),
    ItemData(102, "Nebula Drink: Indefinable Spectrum"),
    ItemData(103, "Nebula Drink: Parasol"),
    ItemData(104, "Nebula Drink: Cool Melon"),
    ItemData(105, "Nebula Drink: Acid's Favorite"),
    ItemData(106, "Nebula Drink: Lost Mountain Water"),
    ItemData(107, "Nebula Drink: Water"),
    ItemData(108, "Nebula Drink: Evening Haze"),
    ItemData(109, "Nebula Drink: Kill The Thirst"),
    ItemData(110, "Nebula Drink: Sanitea"),
    ItemData(111, "Nebula Drink: Crystal Sparkling Water"),
    ItemData(112, "Nebula Drink: O.O.O."),
    ItemData(113, "Nebula Drink: Dead Moon"),
    ItemData(114, "Nebula Drink: Blood Fountain"),
    ItemData(115, "Nebula Drink: Parallel Red"),
    ItemData(116, "Nebula Drink: Aesthestic Water"),
    ItemData(117, "Nebula Drink: Tropical Demolition"),
    ItemData(118, "Nebula Drink: Pillar Flower"),
    ItemData(119, "Nebula Drink: Power of Goat Soda"),
    ItemData(120, "Nebula Drink: Statue Mind"),
    ItemData(121, "Nebula Drink: The Elusive Chocolate"),
    ItemData(122, "Nebula Drink: Bizarre Lychee"),
    ItemData(123, "Nebula Drink: Provocative Flower"),
]

SODA_ID_TO_NAME = {
    item.id: item.name
    for item in SODA_ITEMS
}

SODA_NAME_TO_ID = {
    item.name: item.id
    for item in SODA_ITEMS
}