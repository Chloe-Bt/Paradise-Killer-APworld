from BaseClasses import Item, ItemClassification as ItemClass
from . import ParadiseKillerOptions

from .ItemLists.Keys import *
from .ItemLists.NebulaSodas import *
from .ItemLists.Upgrades import *
from .ItemLists.Whiskys import *
from .ItemLists.Relics import *
from .ItemLists.BloodCrystals import *

from ..AutoWorld import World

class ParadiseKillerItem(Item):
    game = "Paradise Killer"

    def __init__(self, name: str, classification: ItemClass, id: int, player):
        super().__init__(name, classification, id, player)


def get_item_dict():
    result = {}
    '''
    # Sphere inhibitors
    for KEY_ID in ALL_KEY:
        result[KEY_ID_TO_NAME[KEY_ID]] = KEY_ID

    # Nebula Soda Drinks
    for SODA_ID in ALL_SODA:
        result[SODA_ID_TO_NAME[SODA_ID]] = SODA_ID

    # Whisky Bottle
    for WHISKY_ID in ALL_WHISKY:
        result[WHISKY_ID_TO_NAME[WHISKY_ID]] = WHISKY_ID

    # Relics
    for RELIC_ID in ALL_RELIC:
        result[RELIC_ID_TO_NAME[RELIC_ID]] = RELIC_ID
    '''
    
    # Blood Crystals
    for BC_ID in ALL_BC:
        result[BC_ID_TO_NAME[BC_ID]] = BC_ID
    
    # Upgrades
    for UPGRADE_ID in ALL_UPGRADE:
        result[UPGRADE_ID_TO_NAME[UPGRADE_ID]] = UPGRADE_ID

    return result


def populate_item_pool(world: World, options: ParadiseKillerOptions):
    item_count = 0
    location_count = sum(1 for e in world.get_locations())

    item_count += add_full_base_game_items(world, options)
    '''
    if options.enable_nebula_drinks.value:
        for soda_id in ALL_SODA:
            item = ParadiseKillerItem(SODA_ID_TO_NAME[soda_id], ItemClass.progression, soda_id, world.player)
            world.multiworld.itempool.append(item)
            item_count += 1
    
    if options.enable_whisky_bottles.value:
        for whisky_id in ALL_WHISKY:
            item = ParadiseKillerItem(WHISKY_ID_TO_NAME[whisky_id], ItemClass.progression, whisky_id, world.player)
            world.multiworld.itempool.append(item)
            item_count += 1

    if options.enable_mapping_requirements.value:
        for key_id in ALL_KEY:
            item = ParadiseKillerItem(KEY_ID_TO_NAME[key_id], ItemClass.progression, key_id, world.player)
            world.multiworld.itempool.append(item)
            item_count += 1
    '''
    filler = max(0, location_count - item_count)
    
    for _ in range(filler):
        item = ParadiseKillerItem("Blood Crystal (filler)", ItemClass.filler, 1000, world.player)
        world.multiworld.itempool.append(item)


def add_full_base_game_items(world: World, options: ParadiseKillerOptions):
    item_count = 0

    for upgrade_id in ALL_UPGRADE:
        item = ParadiseKillerItem(UPGRADE_ID_TO_NAME[upgrade_id], ItemClass.progression, upgrade_id, world.player)
        world.multiworld.itempool.append(item)
        item_count += 1
    '''
    for relic_id in ALL_RELIC:
        item = ParadiseKillerItem(RELIC_ID_TO_NAME[relic_id], ItemClass.filler, relic_id, world.player)
        world.multiworld.itempool.append(item)
        item_count += 1
    '''
    return item_count

def add_filler(world, options, filler):
    pass

def is_progression(id):
    pass
