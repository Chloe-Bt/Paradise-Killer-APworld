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
    enabled_if: Callable = lambda options: options.enable_shrines
    tags: set[str] = field(default_factory=lambda: {"Carving"})



# Carving Items ID's
CARVING_DH  = 701
CARVING_SG  = 702
CARVING_BD  = 703
CARVING_DR  = 704
CARVING_CD  = 705
CARVING_EM  = 706
CARVING_NR  = 707
CARVING_EB  = 708
CARVING_SL  = 709
CARVING_NN  = 710
CARVING_DFS = 711
CARVING_CG  = 712
CARVING_LP  = 713
CARVING_Z   = 714
CARVING_BS  = 715
CARVING_DE  = 716
CARVING_MP  = 717
CARVING_SZ  = 718
CARVING_VE  = 719



# Carving Items
CARVING_ITEMS = [
    ItemData(
        id=CARVING_DH,
        name="Damned Harmony carving",
    ),
    ItemData(
        id=CARVING_SG,
        name="Silent Goat carving",
    ),
    ItemData(
        id=CARVING_BD,
        name="Blood Dancer carving",
    ),
    ItemData(
        id=CARVING_DR,
        name="Dire Rose carving",
    ),
    ItemData(
        id=CARVING_CD,
        name="Cosmic Deceit carving",
    ),
    ItemData(
        id=CARVING_EM,
        name="Endless Moon carving",
    ),
    ItemData(
        id=CARVING_NR,
        name="Nightmare Revival carving",
    ),
    ItemData(
        id=CARVING_EB,
        name="Enchanted Blue carving",
    ),
    ItemData(
        id=CARVING_SG,
        name="Silent Goat carving",
    ),
    ItemData(
        id=CARVING_NN,
        name="New Night carving",
    ),
    ItemData(
        id=CARVING_DFS,
        name="Dying From Sadness carving",
    ),
    ItemData(
        id=CARVING_CG,
        name="Crying Grudge carving",
    ),
    ItemData(
        id=CARVING_LP,
        name="Lost Pain carving",
    ),
    ItemData(
        id=CARVING_Z,
        name="Zealous carving",
        classification = ItemClassification.progression
    ),
    ItemData(
        id=CARVING_BS,
        name="Beautiful Spectre carving",
    ),
    ItemData(
        id=CARVING_DE,
        name="Destroyed Eden carving",
    ),
    ItemData(
        id=CARVING_MP,
        name="Moonlight Petal carving",
    ),
    ItemData(
        id=CARVING_SZ,
        name="Shadow Zero carving",
    ),
    ItemData(
        id=CARVING_VE,
        name="Vile Embrace carving",
    ),
]

CARVING_ID_TO_NAME = {
    item.id: item.name
    for item in CARVING_ITEMS
}

CARVING_NAME_TO_ID = {
    item.name: item.id
    for item in CARVING_ITEMS
}