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
    enabled_if: Callable = lambda options: options.enable_starlight_skins
    tags: set[str] = field(default_factory=lambda: {"Starlight Skins"})


# Starlight Skins Items ID's



# Starlight Skins Items
STARLIGHTS_ITEMS = [
    ItemData(
        id = 901,
        name = "Starlight Skin: A Billion Stars",
    ),
    ItemData(
        id = 902,
        name = "Starlight Skin: Ancient Battlefield",
    ),
    ItemData(
        id = 903,
        name = "Starlight Skin: Ancient Text",
    ),
    ItemData(
        id = 904,
        name = "Starlight Skin: Aspirational View",
    ),
    ItemData(
        id = 905,
        name = "Starlight Skin: Bathed Towers",
    ),
    ItemData(
        id = 906,
        name = "Starlight Skin: Bear the Shiba",
    ),
    ItemData(
        id = 907,
        name = "Starlight Skin: Beautiful Blossom",
    ),
    ItemData(
        id = 908,
        name = "Starlight Skin: Blazing Sunset",
    ),
    ItemData(
        id = 909,
        name = "Starlight Skin: Blissful Sky",
    ),
    ItemData(
        id = 910,
        name = "Starlight Skin: Bridge to Nowhere",
    ),
    ItemData(
        id = 911,
        name = "Starlight Skin: CD Soundtrack Cover",
    ),
    ItemData(
        id = 912,
        name = "Starlight Skin: Creeping Flora",
    ),
    ItemData(
        id = 913,
        name = "Starlight Skin: Dead Nebula",
    ),
    ItemData(
        id = 914,
        name = "Starlight Skin: Dimensional Breakdown",
    ),
    ItemData(
        id = 915,
        name = "Starlight Skin: End of Day",
    ),
    ItemData(
        id = 916,
        name = "Starlight Skin: Escape to the City",
    ),
    ItemData(
        id = 917,
        name = "Starlight Skin: Final Moments",
    ),
    ItemData(
        id = 918,
        name = "Starlight Skin: Fleeing Moon",
    ),
    ItemData(
        id = 919,
        name = "Starlight Skin: Forbidden City",
    ),
    ItemData(
        id = 920,
        name = "Starlight Skin: Fortified Desert",
    ),
    ItemData(
        id = 921,
        name = "Starlight Skin: Glimpse of Serenity",
    ),
    ItemData(
        id = 922,
        name = "Starlight Skin: Grim Lotus",
    ),
    ItemData(
        id = 923,
        name = "Starlight Skin: Hallowed Bamboo",
    ),
    ItemData(
        id = 924,
        name = "Starlight Skin: Holy Refinery",
    ),
    ItemData(
        id = 925,
        name = "Starlight Skin: Idol Starlight",
    ),
    ItemData(
        id = 926,
        name = "Starlight Skin: Idyllic Beach",
    ),
    ItemData(
        id = 927,
        name = "Starlight Skin: Impassable Space",
    ),
    ItemData(
        id = 928,
        name = "Starlight Skin: Incomprehensible Starlight",
    ),
    ItemData(
        id = 929,
        name = "Starlight Skin: Inscribed in the Surface",
    ),
    ItemData(
        id = 930,
        name = "Starlight Skin: Inverted Pyramid",
    ),
    ItemData(
        id = 931,
        name = "Starlight Skin: Investigation Freak",
    ),
    ItemData(
        id = 932,
        name = "Starlight Skin: Loquacious Jellyfish",
    ),
    ItemData(
        id = 933,
        name = "Starlight Skin: Mysterious Carp",
    ),
    ItemData(
        id = 934,
        name = "Starlight Skin: Pop Art",
    ),
    ItemData(
        id = 935,
        name = "Starlight Skin: Possible Crucible",
    ),
    ItemData(
        id = 936,
        name = "Starlight Skin: Silent Watchers",
    ),
    ItemData(
        id = 937,
        name = "Starlight Skin: Symbol of a Bar Master",
    ),
    ItemData(
        id = 938,
        name = "Starlight Skin: Symbol of a Kiss",
    ),
    ItemData(
        id = 939,
        name = "Starlight Skin: Symbol of the Secretary",
    ),
    ItemData(
        id = 940,
        name = "Starlight Skin: Symbols of a Warrior",
    ),
    ItemData(
        id = 941,
        name = "Starlight Skin: Symbols of an Architect",
    ),
    ItemData(
        id = 942,
        name = "Starlight Skin: Symbols of Day Break",
    ),
    ItemData(
        id = 943,
        name = "Starlight Skin: Symbols of Justice",
    ),
    ItemData(
        id = 944,
        name = "Starlight Skin: Symbols of Medication",
    ),
    ItemData(
        id = 945,
        name = "Starlight Skin: Symbols of Secrets",
    ),
    ItemData(
        id = 946,
        name = "Starlight Skin: Symbols of the Possessed",
    ),
    ItemData(
        id = 947,
        name = "Starlight Skin: Symbols of the Witness",
    ),
    ItemData(
        id = 948,
        name = "Starlight Skin: Terrifying Shallows",
    ),
    ItemData(
        id = 949,
        name = "Starlight Skin: The Day Breaks",
    ),
    ItemData(
        id = 950,
        name = "Starlight Skin: Transmission Tower",
    ),
    ItemData(
        id = 951,
        name = "Starlight Skin: Tropical Starlight",
    ),
    ItemData(
        id = 952,
        name = "Starlight Skin: Verdant",
    ),
    ItemData(
        id = 953,
        name = "Starlight Skin: Vibing",
    ),
    ItemData(
        id = 954,
        name = "Starlight Skin: Warmth of the Moon",
    ),
    ItemData(
        id = 955,
        name = "Starlight Skin: Wonderful Skyline",
    ),
]

STARLIGHTS_ID_TO_NAME = {
    item.id: item.name
    for item in STARLIGHTS_ITEMS
}

STARLIGHTS_NAME_TO_ID = {
    item.name: item.id
    for item in STARLIGHTS_ITEMS
}
