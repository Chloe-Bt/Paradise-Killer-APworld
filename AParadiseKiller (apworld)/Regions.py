from typing import Callable, Optional, Dict

from BaseClasses import Region, Entrance
from . import ParadiseKillerOptions
from . import Items

from .ItemLists.Keys import *
from .ItemLists.Upgrades import *

def create_regions(world, options: ParadiseKillerOptions):
    regions: Dict[str, Region] = \
        {
            "Menu": Region("Menu", world.player, world.multiworld),
            "Idle Lands": Region("Idle Lands", world.player, world.multiworld),
            "Agri Fields": Region("Agri Fields", world.player, world.multiworld),
            "Beach": Region("Beach", world.player, world.multiworld),
            "Citizen Apartments": Region("Citizen Apartments", world.player, world.multiworld),
            "Citizen Housing": Region("Citizen Housing", world.player, world.multiworld),
            "Council Building": Region("Council Building", world.player, world.multiworld),
            "Court House": Region("Court House", world.player, world.multiworld),
            "Danchi": Region("Danchi", world.player, world.multiworld),
            "Dead Zone": Region("Dead Zone", world.player, world.multiworld),
            "Deep Factory Entrance": Region("Deep Factory Entrance", world.player, world.multiworld),
            "Desolation Cell": Region("Desolation Cell", world.player, world.multiworld),
            "Doom Jazz's Yacht": Region("Doom Jazz's Yacht", world.player, world.multiworld),
            "Gardens": Region("Gardens", world.player, world.multiworld),
            "K. HX's Workshop": Region("K. HX's Workshop", world.player, world.multiworld),
            "Marshal Barracks": Region("Marshal Barracks", world.player, world.multiworld),
            "Mountain Gorge": Region("Mountain Gorge", world.player, world.multiworld),
            "Opulent Ziggurat": Region("Opulent Ziggurat", world.player, world.multiworld),
            "Overworld": Region("Overworld", world.player, world.multiworld),
            "Paradise Gates": Region("Paradise Gates", world.player, world.multiworld),
            "Pyramid": Region("Pyramid", world.player, world.multiworld),
            "Reality Folding Drive": Region("Reality Folding Drive", world.player, world.multiworld),
            "Secret Bunker": Region("Secret Bunker", world.player, world.multiworld),
            "Secret Corridor": Region("Secret Corridor", world.player, world.multiworld),
            "Syndicate Apartments": Region("Syndicate Apartments", world.player, world.multiworld),
            "Syndicate Graveyard": Region("Syndicate Graveyard", world.player, world.multiworld),
            "Syndicate HQ": Region("Syndicate HQ", world.player, world.multiworld),
            "Tunnel": Region("Tunnel", world.player, world.multiworld),
        }

    connect(world.player, "menu-to-IL", regions["Menu"], regions["Idle Lands"])

    # Idle Lands
    key_item_name = UPGRADE_ID_TO_NAME[SU_GOAT]
    connect(world.player, "IL-to-O", regions["Idle Lands"], regions["Overworld"],
            lambda state, ki=key_item_name: state.has(ki, world.player))

    # Agri Fields
    key_item_name = KEY_ID_TO_NAME[KEY_AF]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-AF", regions["Overworld"], regions["Agri Fields"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-AF", regions["Overworld"], regions["Agri Fields"])
    connect(world.player, "AF-to-O", regions["Agri Fields"], regions["Overworld"])

    # Beach
    key_item_name = KEY_ID_TO_NAME[KEY_B]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-B", regions["Overworld"], regions["Beach"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-B", regions["Overworld"], regions["Beach"])
    connect(world.player, "B-to-O", regions["Beach"], regions["Overworld"])

    # Citizen Apartments
    key_item_name = KEY_ID_TO_NAME[KEY_CA]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-CA", regions["Overworld"], regions["Citizen Apartments"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-CA", regions["Overworld"], regions["Citizen Apartments"])
    connect(world.player, "CA-to-O", regions["Citizen Apartments"], regions["Overworld"])

    # Citizen Housing
    key_item_name = KEY_ID_TO_NAME[KEY_CH]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-CH", regions["Overworld"], regions["Citizen Housing"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-CH", regions["Overworld"], regions["Citizen Housing"])
    connect(world.player, "CH-to-O", regions["Citizen Housing"], regions["Overworld"])

    # Council Building
    key_item_name = KEY_ID_TO_NAME[KEY_CB]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-CB", regions["Overworld"], regions["Council Building"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-CB", regions["Overworld"], regions["Council Building"])
    connect(world.player, "CB-to-O", regions["Council Building"], regions["Overworld"])

    # Court House
    key_item_name = KEY_ID_TO_NAME[KEY_CHC]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-CHC", regions["Overworld"], regions["Court House"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-CHC", regions["Overworld"], regions["Court House"])
    connect(world.player, "CHC-to-O", regions["Court House"], regions["Overworld"])

    # Danchi
    key_item_name = KEY_ID_TO_NAME[KEY_D]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-D", regions["Overworld"], regions["Danchi"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-D", regions["Overworld"], regions["Danchi"])
    connect(world.player, "D-to-O", regions["Danchi"], regions["Overworld"])

    # Deep Factory Entrance
    key_item_name = KEY_ID_TO_NAME[KEY_DFE]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-DFE", regions["Overworld"], regions["Deep Factory Entrance"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-DFE", regions["Overworld"], regions["Deep Factory Entrance"])
    connect(world.player, "DFE-to-O", regions["Deep Factory Entrance"], regions["Overworld"])

    # Gardens
    key_item_name = KEY_ID_TO_NAME[KEY_G]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-G", regions["Overworld"], regions["Gardens"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-G", regions["Overworld"], regions["Gardens"])
    connect(world.player, "G-to-O", regions["Gardens"], regions["Overworld"])

    # K. HX's Workshop
    key_item_name = KEY_ID_TO_NAME[KEY_KHX]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-KHX", regions["Overworld"], regions["K. HX's Workshop"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-KHX", regions["Overworld"], regions["K. HX's Workshop"])
    connect(world.player, "KHX-to-O", regions["K. HX's Workshop"], regions["Overworld"])

    # Mountain Gorge
    key_item_name = KEY_ID_TO_NAME[KEY_MG]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-MG", regions["Overworld"], regions["Mountain Gorge"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-MG", regions["Overworld"], regions["Mountain Gorge"])
    connect(world.player, "MG-to-O", regions["Mountain Gorge"], regions["Overworld"])

    # Opulent Ziggurat
    key_item_name = KEY_ID_TO_NAME[KEY_OZ]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-OZ", regions["Overworld"], regions["Opulent Ziggurat"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-OZ", regions["Overworld"], regions["Opulent Ziggurat"])
    connect(world.player, "OZ-to-O", regions["Opulent Ziggurat"], regions["Overworld"])

    # Paradise Gates
    key_item_name = KEY_ID_TO_NAME[KEY_PG]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-PG", regions["Overworld"], regions["Paradise Gates"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-PG", regions["Overworld"], regions["Paradise Gates"])
    connect(world.player, "PG-to-O", regions["Paradise Gates"], regions["Overworld"])

    # Pyramid
    key_item_name = KEY_ID_TO_NAME[KEY_P]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-P", regions["Overworld"], regions["Pyramid"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-P", regions["Overworld"], regions["Pyramid"])
    connect(world.player, "P-to-O", regions["Pyramid"], regions["Overworld"])

    # Reality Folding Drive
    key_item_name = KEY_ID_TO_NAME[KEY_RFD]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-RFD", regions["Overworld"], regions["Reality Folding Drive"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-RFD", regions["Overworld"], regions["Reality Folding Drive"])
    connect(world.player, "RFD-to-O", regions["Reality Folding Drive"], regions["Overworld"])

    # Secret Corridor
    connect(world.player, "O-to-SC", regions["Overworld"], regions["Secret Corridor"])
    connect(world.player, "SC-to-O", regions["Secret Corridor"], regions["Overworld"])
    
    # Syndicate Apartments
    key_item_name = KEY_ID_TO_NAME[KEY_SA]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-SA", regions["Overworld"], regions["Syndicate Apartments"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-SA", regions["Overworld"], regions["Syndicate Apartments"])
    connect(world.player, "SA-to-O", regions["Syndicate Apartments"], regions["Overworld"])

    # Syndicate Graveyard
    key_item_name = KEY_ID_TO_NAME[KEY_SG]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-SG", regions["Overworld"], regions["Syndicate Graveyard"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-SG", regions["Overworld"], regions["Syndicate Graveyard"])
    connect(world.player, "SG-to-O", regions["Syndicate Graveyard"], regions["Overworld"])

    # Syndicate HQ
    key_item_name = KEY_ID_TO_NAME[KEY_SHQ]
    if options.enable_mapping_requirements == 1:
        connect(world.player, "O-to-SHQ", regions["Overworld"], regions["Syndicate HQ"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    else:
        connect(world.player, "O-to-SHQ", regions["Overworld"], regions["Syndicate HQ"])
    connect(world.player, "SHQ-to-O", regions["Syndicate HQ"], regions["Overworld"])

    # Tunnel
    key_item_name = UPGRADE_ID_TO_NAME[SU_COSMOS]
    connect(world.player, "O-to-T", regions["Overworld"], regions["Tunnel"],
            lambda state, ki=key_item_name: state.has(ki, world.player))
    connect(world.player, "T-to-O", regions["Tunnel"], regions["Overworld"])

    return regions


def connect(player: int, name: str, source_region: Region, target_region: Region, rule: Optional[Callable] = None):
    connection = Entrance(player, name, source_region)

    if rule is not None:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

    return connection
