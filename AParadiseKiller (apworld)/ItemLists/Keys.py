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
    tags: set[str] = field(default_factory=lambda: {"Keys"})



# Keys Items ID's
KEY_AF      = 301
KEY_B       = 302
KEY_CA      = 303
KEY_CH      = 304
KEY_CB      = 305
KEY_CHC     = 306
KEY_D       = 307
KEY_DFE     = 308
KEY_G       = 309
KEY_KHX     = 310
KEY_MG      = 311
KEY_OZ      = 312
KEY_PG      = 313
KEY_P       = 314
KEY_RFD     = 315
KEY_SA      = 316
KEY_SG      = 317
KEY_SHQ     = 318
KEY_DJY     = 319
KEY_DC      = 320
KEY_MB      = 321
KEY_DZ      = 322

SKEY_DT     = 330
SKEY_SL     = 331
SKEY_AL     = 332



# Keys Items ID's
KEY_ITEMS = [
    ItemData(
        id=KEY_AF,
        name="Farming Supplies (unlock the Agri Fields area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_B,
        name="Beach Towel (unlock the Beach area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_CA,
        name="Appartement Key (unlock the Citizen Apartments area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_CH,
        name="House Key (unlock the Citizen Housing area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_CB,
        name="Syndicate Pamphlet (unlock the Council Building area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_CHC,
        name="Letter of Jury Duty (unlock the Court House area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_D,
        name="Fishing Rod (unlock the Danchi area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_DFE,
        name="Employee Card (unlock the Deep Factory Entrance area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_G,
        name="Gardening Supplies (unlock the Gardens area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_KHX,
        name="HX's Spare Keys (unlock the K. HX's Workshop area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_MG,
        name="Goat, no not that goat (unlock the Mountain Gorge area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_OZ,
        name="Holy Scriptures (unlock the Opulent Ziggurat area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_PG,
        name="The Great Key (unlock the Paradise Gates area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_P,
        name="Jetsky (unlock the Pyramid area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_RFD,
        name="Hard Hat (unlock the Reality Folding Drive area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_DJY,
        name="Yacht License (unlock the Doom Jazz's Yacht area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_SA,
        name="Master Key (unlock the Syndicate Apartments area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_SG,
        name="Syndicate Tear (unlock the Syndicate Graveyard area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_SHQ,
        name="Control Room Access (unlock the Syndicate HQ area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_DC,
        name="Prison Pass (unlock the Desolation Cell area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_MB,
        name="Ensignia (unlock the Marshal Barracks area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    ItemData(
        id=KEY_DZ,
        name="Gas Mask (unlock the Dead Zone area)",
        enabled_if=lambda options: options.enable_mapping_requirements,
    ),
    
    
    
    
    ItemData(
        id=SKEY_DT,
        name="Demon Translator (unlocks Shinji locations)",
        enabled_if=lambda options: options.enable_shinji_locations,
    ),
    ItemData(
        id=SKEY_SL,
        name="Soda License (unlock ability to buy soda cans)",
        enabled_if=lambda options: options.enable_soda_license,
    ),
    ItemData(
        id=SKEY_AL,
        name="Alcohol License (unlock ability to get whisky bottles)",
        enabled_if=lambda options: options.enable_alcohol_license,
    ),
]

KEY_ID_TO_NAME = {
    item.id: item.name
    for item in KEY_ITEMS
}

KEY_NAME_TO_ID = {
    item.name: item.id
    for item in KEY_ITEMS
}