from BaseClasses import Item, ItemClassification as ItemClass
from . import ParadiseKillerOptions

from .ItemLists.Keys import *
from .ItemLists.NebulaSodas import *
from .ItemLists.Upgrades import *
from .ItemLists.Whiskys import *
from .ItemLists.Relics import *
from .ItemLists.BloodCrystals import *
from .ItemLists.Crests import *
from .ItemLists.IslandMomentos import *
from .ItemLists.Carvings import *
from .ItemLists.Recordings import *
from .ItemLists.StarlightSkins import *
from .ItemLists.KeyItems import *
from .ItemLists.BloodCrystals import *
from .ItemLists.RadioControlTowers import *
from .ItemLists.Keys import *

from .Locations import *

from ..AutoWorld import World

class ParadiseKillerItem(Item):
    game = "Paradise Killer"

    def __init__(self, name: str, classification: ItemClass, id: int, player):
        super().__init__(name, classification, id, player)


def get_item_dict():
    return {item.name: item.id for item in get_all_items()}


def populate_item_pool(world: World, options: ParadiseKillerOptions):
    enabled_items  = get_enabled_items(options)
    
    location_count = len(get_enabled_locations(options))
    item_count     = sum(item.copies for item in get_enabled_items(options))

    #print(f"Number of locations: {location_count}")
    #print(f"Number of items: {item_count}")

    itempool = []

    for item_data in get_enabled_items(options):
        classification = (
            item_data.classification(options)
            if callable(item_data.classification)
            else item_data.classification
        )
        for _ in range(item_data.copies):
            itempool.append(
                ParadiseKillerItem(
                    item_data.name, 
                    classification, 
                    item_data.id, 
                    world.player
                )
            )
            
    excess = item_count - location_count
    if excess > 0:
        relic_names = {item.name for item in RELIC_ITEMS}
        removable = [
            index
            for index, item in enumerate(itempool)
            if (
                item.name in relic_names and item.classification == ItemClass.filler
            )
        ]
        world.random.shuffle(removable)
        for index in reversed(removable[:excess]):
            removed = itempool.pop(index)
            #print(f"Removed filler Relic: {removed.name}")
            
    elif excess < 0:
        filler = ParadiseKillerItem(
            "Blood Crystal",
            ItemClass.filler, 
            1000, 
            world.player
        )
        for _ in range(-1*excess):
            itempool.append(filler)
    
    world.multiworld.itempool.extend(itempool)


def ItemClassification(options):
    return {name for name, value in vars(options).items() if value is True}


def get_enabled_items(options):
    result = []
    for item in get_all_items():
        if item.enabled_if and not item.enabled_if(options):
            continue
        result.append(item)
    return result


def get_all_items():
    ALL_ITEMS = (
        WHISKY_ITEMS
        + SODA_ITEMS
        + UPGRADE_ITEMS
        + KEY_ITEMS
        + IM_ITEMS
        + CREST_ITEMS
        + CARVING_ITEMS
        + RECORDING_ITEMS
        + STARLIGHTS_ITEMS
        + KI_ITEMS
        + RELIC_ITEMS
        + BC_ITEMS
        + RADIO_ITEMS
    )
    return ALL_ITEMS