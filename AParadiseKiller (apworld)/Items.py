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
from .ItemLists.BloodCrystals import *
from .ItemLists.KeyItems import *
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

    soda_item_ids = {item.id for item in SODA_ITEMS}
    whisky_item_ids = {item.id for item in WHISKY_ITEMS}

    soda_ids = set()
    whisky_ids = set()
    if options.goal.value == options.goal.option_lady_soda_dies:
        soda_ids = get_required_soda_ids(world, options, enabled_items)
    elif options.goal.value == options.goal.option_lady_whisky_dies:
        whisky_ids = get_required_whisky_ids(world, options, enabled_items)

    itempool = []

    for item_data in enabled_items:
        if options.goal.value == options.goal.option_lady_soda_dies and item_data.id in soda_item_ids:
            classification = (
                ItemClass.progression
                if item_data.id in soda_ids
                else ItemClass.useful
            )

        elif options.goal.value == options.goal.option_lady_whisky_dies and item_data.id in whisky_item_ids:
            classification = (
                ItemClass.progression
                if item_data.id in whisky_ids
                else ItemClass.useful
            )

        else:
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
            item for item in itempool
            if (
                item.name in relic_names and item.classification == ItemClass.filler
            )
        ]
        world.random.shuffle(removable)
        
        for item in removable[:excess]:
            itempool.remove(item)
            print(f"Removed filler Relic: {item.name}")
            
    elif excess < 0:
        for _ in range(-1*excess):
            itempool.append(ParadiseKillerItem(
                "Blood Crystal",
                ItemClass.filler, 
                1000, 
                world.player
            )
        )
        
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
        + BC_ITEMS
        + RELIC_ITEMS
        + RADIO_ITEMS
    )
    return ALL_ITEMS


def get_required_soda_ids(world: World, options: ParadiseKillerOptions, enabled_items):
    soda_progression_ids = set()
    soda_ids = {item.id for item in SODA_ITEMS}
    required_soda = options.number_nebula_drinks.value
    soda_candidates = [item for item in enabled_items if item.id in soda_ids]
    soda_progression_ids = {item.id for item in world.random.sample(soda_candidates, required_soda)}
    return soda_progression_ids

def get_required_whisky_ids(world: World, options: ParadiseKillerOptions, enabled_items):
    whisky_progression_ids = set()
    whisky_ids = {item.id for item in WHISKY_ITEMS}
    required_whisky = options.number_whisky_bottles.value
    whisky_candidates = [item for item in enabled_items if item.id in whisky_ids]
    whisky_progression_ids = {item.id for item in world.random.sample(whisky_candidates, required_whisky)}
    return whisky_progression_ids