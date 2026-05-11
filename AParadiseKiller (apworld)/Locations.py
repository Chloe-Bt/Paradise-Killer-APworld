from typing import Dict

from BaseClasses import Location, Region
from ..AutoWorld import World
from ..generic.Rules import add_rule

from . import ParadiseKillerOptions

from .ItemLists.Upgrades import *
from .ItemLists.Keys import *
from .ItemLists.NebulaSodas import *
from .ItemLists.Whiskys import *

from .LocationLists.AgriFields import *
from .LocationLists.Beach import *
from .LocationLists.CitizenApartments import *
from .LocationLists.CitizenHousing import *
from .LocationLists.CouncilBuilding import *
from .LocationLists.CourtHouse import *
from .LocationLists.Danchi import *
from .LocationLists.DeadZone import *
from .LocationLists.DeepFactoryEntrance import *
from .LocationLists.DesolationCell import *
from .LocationLists.DoomJazzYacht import *
from .LocationLists.Gardens import *
from .LocationLists.IdleLands import *
from .LocationLists.KHXWorkshop import *
from .LocationLists.MarshalBarracks import *
from .LocationLists.MountainGorge import *
from .LocationLists.OpulentZiggurat import *
from .LocationLists.Overworld import *
from .LocationLists.ParadiseGates import *
from .LocationLists.Pyramid import *
from .LocationLists.RealityFoldingDrive import *
from .LocationLists.SecretBunker import *
from .LocationLists.SecretCorridor import *
from .LocationLists.SyndicateApartments import *
from .LocationLists.SyndicateGraveyard import *
from .LocationLists.SyndicateHQ import *
from .LocationLists.Tunnel import *

class ParadiseKillerLocation(Location):
    game: str = "Paradise Killer"

    def __init__(self, player, location_name, location_id, region):
        super().__init__(player, location_name, location_id, region)

def get_location_dict():
    return {
        loc.name: loc.id
        for loc in get_all_locations()
    }

def create_locations(world: World, regions: Dict[str, Region], options: ParadiseKillerOptions):
    for loc_data in get_enabled_locations(options):
        region = regions[loc_data.region]

        loc = ParadiseKillerLocation(
            world.player,
            loc_data.name,
            loc_data.id,
            region
        )

        if loc_data.rule:
            add_rule(
                loc,
                lambda state, rule=loc_data.rule: rule(state, options, world.player)
            )

        region.locations.append(loc)

def get_enabled_settings(options):
    enabled_settings = set()

    if options.enable_nebula_drinks:
        enabled_settings.add("enable_nebula_drinks")

    if options.enable_whisky_bottles:
        enabled_settings.add("enable_whisky_bottles")
    
    if options.enables_shinji_locations:
        enabled_settings.add("enable_shinji_locations")
    
    if options.enable_starlight_skins:
        enabled_settings.add("enable_starlight_skins")
    
    if options.enable_island_momentos:
        enabled_settings.add("enable_island_momentos")
    
    if options.enable_music_tracks:
        enabled_settings.add("enable_music_tracks")
    
    if options.enable_shrines:
        enabled_settings.add("enable_shrines")
    
    if options.enable_recordings:
        enabled_settings.add("enable_recordings")

    return enabled_settings

def get_enabled_locations(options):
    result = []

    for loc in get_all_locations():
        if loc.enabled_if and not loc.enabled_if(options):
            continue

        result.append(loc)

    return result

def get_all_locations():
    ALL_LOCATIONS = (
        AF_LOCATIONS
        + IL_LOCATIONS
        + DZ_LOCATIONS
        + B_LOCATIONS
        + CA_LOCATIONS
        + CH_LOCATIONS
        + CB_LOCATIONS
        + CHC_LOCATIONS
        + D_LOCATIONS
        + DFE_LOCATIONS
        + DC_LOCATIONS
        + DJY_LOCATIONS
        + G_LOCATIONS
        + KHX_LOCATIONS
        + MB_LOCATIONS
        + MG_LOCATIONS
        + OZ_LOCATIONS
        + PG_LOCATIONS
        + P_LOCATIONS
        + RFD_LOCATIONS
        + SC_LOCATIONS
        + SA_LOCATIONS
        + SG_LOCATIONS
        + SHQ_LOCATIONS
    )
    return ALL_LOCATIONS