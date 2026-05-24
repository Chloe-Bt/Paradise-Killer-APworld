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
    enabled_if: Callable = lambda options: options.enable_music_tracks
    tags: set[str] = field(default_factory=lambda: {"Radio Control Tower"})



# Radio Control Tower Items
RADIO_ITEMS = [
    ItemData(1401, "Music Track: Leaving"),
    ItemData(1402, "Music Track: End of the World"),
    ItemData(1403, "Music Track: To The Heart"),
    ItemData(1404, "Music Track: Midori Eyes"),
    ItemData(1405, "Music Track: Lady Blue"),
    ItemData(1406, "Music Track: Sunset Song"),
    ItemData(1407, "Music Track: Last Dance XX"),
    ItemData(1408, "Music Track: Ego 24-7"),
    ItemData(1409, "Music Track: 8th Street Rose"),
    ItemData(1410, "Music Track: House of Bliss"),
    ItemData(1411, "Music Track: The Lemegeton Bop"),
    ItemData(1412, "Music Track: Unlimited∞Luv"),
    ItemData(1413, "Music Track: Headlights on the Shore"),
    ItemData(1414, "Music Track: About That..."),
    ItemData(1415, "Music Track: Go! Go! Style", classification = ItemClassification.progression),
    ItemData(1416, "Music Track: Citizen Apartments"),
]

RADIO_ID_TO_NAME = {
    item.id: item.name
    for item in RADIO_ITEMS
}

RADIO_NAME_TO_ID = {
    item.name: item.id
    for item in RADIO_ITEMS
}




