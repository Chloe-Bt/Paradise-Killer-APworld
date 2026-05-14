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

from ..AutoWorld import World

class ParadiseKillerItem(Item):
    game = "Paradise Killer"
    def __init__(self, name: str, classification: ItemClass, id: int, player):
        super().__init__(name, classification, id, player)

def get_item_dict():
    return {
        item.name: item.id
        for item in get_all_items()
    }

def populate_item_pool(world: World, options: ParadiseKillerOptions):
    for item_data in get_enabled_items(options):
        classification = (
            item_data.classification(options)
            if callable(item_data.classification)
            else item_data.classification
        )
        for _ in range(item_data.copies):
            item = ParadiseKillerItem(
                item_data.name,
                classification,
                item_data.id,
                world.player
            )
            world.multiworld.itempool.append(item)
            
    filler_needed = len(world.get_locations()) - len(world.multiworld.itempool)
    filler = ParadiseKillerItem("Blood Crystal", ItemClassification.filler, 1000, world.player)
    for i in range(filler_needed):
        world.multiworld.itempool.append(filler)

def get_enabled_settings(options):
    return {
        name
        for name, value in vars(options).items()
        if value is True
    }

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
    )
    return ALL_ITEMS

