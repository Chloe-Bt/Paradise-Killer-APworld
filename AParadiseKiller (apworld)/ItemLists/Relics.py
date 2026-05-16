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
    enabled_if: Callable | None = None
    tags: set[str] = field(default_factory=lambda: {"Relic"})



# Relic Items
RELIC_ITEMS = [
    ItemData(
    id = 1301,
    name = "Locker Code",
    classification = ItemClassification.progression
    ),
    ItemData(
        id = 1302,
        name = "Protest Letter",
        classification = ItemClassification.progression
    ),
    ItemData(
        id = 1303,
        name = "Vampire Report",
        classification = ItemClassification.progression
    ),
    ItemData(
        id = 1304,
        name = "Imperfect Dominoes",
        classification = ItemClassification.progression
    ),
    ItemData(
        id = 1305,
        name = "Fascinating Grasshopper",
    ),
    ItemData(
        id = 1306,
        name = "Playful Stones",
    ),
    ItemData(
        id = 1307,
        name = "Quivering Jellyfish",
    ),
    ItemData(
        id = 1308,
        name = "Wistful Photo",
    ),
    ItemData(
        id = 1309,
        name = "Dulled Percolator",
    ),
    ItemData(
        id = 1310,
        name = "Well-read Book",
    ),
    ItemData(
        id = 1311,
        name = "Desirable Bear Chan Phone Charm",
    ),
    ItemData(
        id = 1312,
        name = "Grubby Skimming Runes",
    ),
    ItemData(
        id = 1313,
        name = "Devil Nebula",
    ),
    ItemData(
        id = 1314,
        name = "Inquisitive Apartment Murder Report",
    ),
    ItemData(
        id = 1315,
        name = "Efficacious Chillies",
    ),
    ItemData(
        id = 1316,
        name = "Discarded Pistachios",
    ),
    ItemData(
        id = 1317,
        name = "Gleaming Male Idol Card",
    ),
    ItemData(
        id = 1318,
        name = "Joyous Fish Food",
    ),
    ItemData(
        id = 1319,
        name = "Glinting Golden Crown",
    ),
    ItemData(
        id = 1320,
        name = "Gaudy Blood Pendant",
    ),
    ItemData(
        id = 1321,
        name = "Suspicious Video Tape",
    ),
    ItemData(
        id = 1322,
        name = "Cheerful Children's Book",
    ),
    ItemData(
        id = 1323,
        name = "Fancy Playing Cards",
    ),
    ItemData(
        id = 1324,
        name = "Extrinsic Fossil",
    ),
    ItemData(
        id = 1325,
        name = "Dazzling Obelisk charm",
    ),
    ItemData(
        id = 1326,
        name = "Absurd Message Stones",
    ),
    ItemData(
        id = 1327,
        name = "Malicious Secretive Cassette",
    ),
    ItemData(
        id = 1328,
        name = "Ill-fated Ring Pulls",
    ),
    ItemData(
        id = 1329,
        name = "Righteous Monserrat T-Shirt",
    ),
    ItemData(
        id = 1330,
        name = "Enchanting Blood Charm",
    ),
    ItemData(
        id = 1331,
        name = "Covetable Workers Reward",
    ),
    ItemData(
        id = 1332,
        name = "Proud Pin Badge",
    ),
    ItemData(
        id = 1333,
        name = "Lurid Crimson Acid Phone Charm",
    ),
    ItemData(
        id = 1334,
        name = "Questionable Donation",
    ),
    ItemData(
        id = 1335,
        name = "Resonant Photo of a Man",
    ),
    ItemData(
        id = 1336,
        name = "Wonderful Crystallized Tears",
    ),
    ItemData(
        id = 1337,
        name = "Nostalgic Fallen Rose",
    ),
    ItemData(
        id = 1338,
        name = "Abnormal Butterfly",
    ),
    ItemData(
        id = 1339,
        name = "Polished Badge",
    ),
    ItemData(
        id = 1340,
        name = "Wistful Lovers Padlock",
    ),
    ItemData(
        id = 1341,
        name = "Incoherent Abandoned Diary",
    ),
    ItemData(
        id = 1342,
        name = "Recondite Ornate Book",
    ),
    ItemData(
        id = 1343,
        name = "Knowledgeable Listening Device",
    ),
    ItemData(
        id = 1344,
        name = "Tawdry Poster",
    ),
    ItemData(
        id = 1345,
        name = "Dazzling Obelisk Charm",
    ),
    ItemData(
        id = 1346,
        name = "Descriptive River Power Station Schedule",
    ),
    ItemData(
        id = 1347,
        name = "Exclusive Silent Goat Carving",
    ),
    ItemData(
        id = 1348,
        name = "Inaccurate Alarm Clock",
    ),
    ItemData(
        id = 1349,
        name = "Coveted Loyalty Card",
    ),
    ItemData(
        id = 1350,
        name = "Obsequious Love Letter",
    ),
    ItemData(
        id = 1351,
        name = "Duplicated Rotten Eggs",
    ),
    ItemData(
        id = 1352,
        name = "Fashionable Dead Nebula Phone Charm",
    ),
    ItemData(
        id = 1353,
        name = "Idiotic Loyalty Levels",
    ),
    ItemData(
        id = 1354,
        name = "Wretched CD",
    ),
    ItemData(
        id = 1355,
        name = "Unavoidable Pain Pills",
    ),
    ItemData(
        id = 1356,
        name = "Glittering Sequin Ward",
    ),
    ItemData(
        id = 1357,
        name = "Shameful Fake Golden Crown",
    ),
    ItemData(
        id = 1358,
        name = "Grotesque Pyramid Charms",
    ),
    ItemData(
        id = 1359,
        name = "Haunting Sculpture",
    ),
    ItemData(
        id = 1360,
        name = "Nauseating Offering Gems",
    ),
    ItemData(
        id = 1363,
        name = "Contemplative Painting",
    ),
    ItemData(
        id = 1364,
        name = "Cute Tamago Phone Charm",
    ),
    ItemData(
        id = 1365,
        name = "Tremendous Game Cart",
    ),
    ItemData(
        id = 1366,
        name = "Vapid Book",
    ),
    ItemData(
        id = 1367,
        name = "Splendid Pamphlet",
    ),
    ItemData(
        id = 1368,
        name = "Fantastic Crystallized Tear Necklace",
    ),
    ItemData(
        id = 1369,
        name = "Lucky Doll",
    ),
    ItemData(
        id = 1370,
        name = "Time Worn Blood Bowl",
    ),
    ItemData(
        id = 1371,
        name = "Maddening Rare Plant",
    ),
    ItemData(
        id = 1372,
        name = "Aromatic Mushrooms",
    ),
    ItemData(
        id = 1373,
        name = "Ill-Fated Pleading Letter",
    ),
    ItemData(
        id = 1374,
        name = "Ultimate Tea",
    ),
    ItemData(
        id = 1375,
        name = "Well Loved Secateurs",
    ),
    ItemData(
        id = 1376,
        name = "Polite Luxury Chocolates",
    ),
    ItemData(
        id = 1377,
        name = "Despairing Diary",
    ),
]

RELIC_ID_TO_NAME = {
    item.id: item.name
    for item in RELIC_ITEMS
}

RELIC_NAME_TO_ID = {
    item.name: item.id
    for item in RELIC_ITEMS
}



