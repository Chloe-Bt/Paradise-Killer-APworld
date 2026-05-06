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
    result = {}

    # Idle Lands
    for IL_ID in ALL_IL:
        result[IL_ID_TO_NAME[IL_ID]] = IL_ID
    '''
    # Agri Fields
    for AF_ID in ALL_AF:
        result[AF_ID_TO_NAME[AF_ID]] = AF_ID

    # Beach
    for B_ID in ALL_B:
        result[B_ID_TO_NAME[B_ID]] = B_ID

    # Citizen Apartments
    for CA_ID in ALL_CA:
        result[CA_ID_TO_NAME[CA_ID]] = CA_ID

    # Citizen Housing
    for CH_ID in ALL_CH:
        result[CH_ID_TO_NAME[CH_ID]] = CH_ID

    # Council Building
    for CB_ID in ALL_CB:
        result[CB_ID_TO_NAME[CB_ID]] = CB_ID

    # Court House
    for CH_COURT_ID in ALL_CH_COURT:
        result[CH_COURT_ID_TO_NAME[CH_COURT_ID]] = CH_COURT_ID

    # Danchi
    for D_ID in ALL_D:
        result[D_ID_TO_NAME[D_ID]] = D_ID

    # Dead Zone
    for DZ_ID in ALL_DZ:
        result[DZ_ID_TO_NAME[DZ_ID]] = DZ_ID

    # Deep Factory Entrance
    for DFE_ID in ALL_DFE:
        result[DFE_ID_TO_NAME[DFE_ID]] = DFE_ID

    # Desolation Cell
    for DS_ID in ALL_DS:
        result[DS_ID_TO_NAME[DS_ID]] = DS_ID

    # Doom Jazz's Yacht
    for DJY_ID in ALL_DJY:
        result[DJY_ID_TO_NAME[DJY_ID]] = DJY_ID

    # Gardens
    for G_ID in ALL_G:
        result[G_ID_TO_NAME[G_ID]] = G_ID

    # K. HX's Workshop
    for KHX_ID in ALL_KHX:
        result[KHX_ID_TO_NAME[KHX_ID]] = KHX_ID

    # Marshal Barracks
    for MB_ID in ALL_MB:
        result[MB_ID_TO_NAME[MB_ID]] = MB_ID

    # Mountain Gorge
    for MG_ID in ALL_MG:
        result[MG_ID_TO_NAME[MG_ID]] = MG_ID

    # Opulent Ziggurat
    for OZ_ID in ALL_OZ:
        result[OZ_ID_TO_NAME[OZ_ID]] = OZ_ID

    # Overworld
    for O_ID in ALL_O:
        result[O_ID_TO_NAME[O_ID]] = O_ID

    # Paradise Gates
    for PG_ID in ALL_PG:
        result[PG_ID_TO_NAME[PG_ID]] = PG_ID

    # Pyramid
    for P_ID in ALL_P:
        result[P_ID_TO_NAME[P_ID]] = P_ID

    # Reality Folding Drive
    for RFD_ID in ALL_RFD:
        result[RFD_ID_TO_NAME[RFD_ID]] = RFD_ID

    # Secret Bunker
    for SB_ID in ALL_SB:
        result[SB_ID_TO_NAME[SB_ID]] = SB_ID

    # Secret Corridor
    for SC_ID in ALL_SC:
        result[SC_ID_TO_NAME[SC_ID]] = SC_ID

    # Syndicate Apartments
    for SA_ID in ALL_SA:
        result[SA_ID_TO_NAME[SA_ID]] = SA_ID

    # Syndicate Graveyard
    for SG_ID in ALL_SG:
        result[SG_ID_TO_NAME[SG_ID]] = SG_ID

    # Syndicate HQ
    for SHQ_ID in ALL_SHQ:
        result[SHQ_ID_TO_NAME[SHQ_ID]] = SHQ_ID

    # Tunnel
    for T_ID in ALL_T:
        result[T_ID_TO_NAME[T_ID]] = T_ID
    '''
    return result

def create_locations(world: World, regions: Dict[str, Region], options: ParadiseKillerOptions):
    # Idle Lands
    IL_region = regions["Idle Lands"]
    for IL_ID in ALL_IL:
        loc = ParadiseKillerLocation(world.player, IL_ID_TO_NAME[IL_ID], IL_ID, IL_region)
        IL_region.locations.append(loc)
    '''
    # Agri Fields
    AF_region = regions["Agri Fields"]
    for AF_ID in ALL_AF:
        loc = ParadiseKillerLocation(world.player, AF_ID_TO_NAME[AF_ID], AF_ID, AF_region)
        AF_region.locations.append(loc)

    # Beach
    B_region = regions["Beach"]
    for B_ID in ALL_B:
        loc = ParadiseKillerLocation(world.player, B_ID_TO_NAME[B_ID], B_ID, B_region)
        B_region.locations.append(loc)

    # Citizen Apartments
    CA_region = regions["Citizen Apartments"]
    for CA_ID in ALL_CA:
        loc = ParadiseKillerLocation(world.player, CA_ID_TO_NAME[CA_ID], CA_ID, CA_region)
        CA_region.locations.append(loc)

    # Citizen Housing
    CH_region = regions["Citizen Housing"]
    for CH_ID in ALL_CH:
        loc = ParadiseKillerLocation(world.player, CH_ID_TO_NAME[CH_ID], CH_ID, CH_region)
        CH_region.locations.append(loc)

    # Council Building
    CB_region = regions["Council Building"]
    for CB_ID in ALL_CB:
        loc = ParadiseKillerLocation(world.player, CB_ID_TO_NAME[CB_ID], CB_ID, CB_region)
        CB_region.locations.append(loc)

    # Court House
    CH_COURT_region = regions["Court House"]
    for CH_COURT_ID in ALL_CH_COURT:
        loc = ParadiseKillerLocation(world.player, CH_COURT_ID_TO_NAME[CH_COURT_ID], CH_COURT_ID, CH_COURT_region)
        CH_COURT_region.locations.append(loc)

    # Danchi
    D_region = regions["Danchi"]
    for D_ID in ALL_D:
        loc = ParadiseKillerLocation(world.player, D_ID_TO_NAME[D_ID], D_ID, D_region)
        D_region.locations.append(loc)

    # Dead Zone
    DZ_region = regions["Dead Zone"]
    for DZ_ID in ALL_DZ:
        loc = ParadiseKillerLocation(world.player, DZ_ID_TO_NAME[DZ_ID], DZ_ID, DZ_region)
        DZ_region.locations.append(loc)

    # Deep Factory Entrance
    DFE_region = regions["Deep Factory Entrance"]
    for DFE_ID in ALL_DFE:
        loc = ParadiseKillerLocation(world.player, DFE_ID_TO_NAME[DFE_ID], DFE_ID, DFE_region)
        DFE_region.locations.append(loc)

    # Desolation Cell
    DS_region = regions["Desolation Cell"]
    for DS_ID in ALL_DS:
        loc = ParadiseKillerLocation(world.player, DS_ID_TO_NAME[DS_ID], DS_ID, DS_region)
        DS_region.locations.append(loc)

    # Doom Jazz's Yacht
    DJY_region = regions["Doom Jazz's Yacht"]
    for DJY_ID in ALL_DJY:
        loc = ParadiseKillerLocation(world.player, DJY_ID_TO_NAME[DJY_ID], DJY_ID, DJY_region)
        DJY_region.locations.append(loc)

    # Gardens
    G_region = regions["Gardens"]
    for G_ID in ALL_G:
        loc = ParadiseKillerLocation(world.player, G_ID_TO_NAME[G_ID], G_ID, G_region)
        G_region.locations.append(loc)

    # K. HX's Workshop
    KHX_region = regions["K. HX's Workshop"]
    for KHX_ID in ALL_KHX:
        loc = ParadiseKillerLocation(world.player, KHX_ID_TO_NAME[KHX_ID], KHX_ID, KHX_region)
        KHX_region.locations.append(loc)

    # Marshal Barracks
    MB_region = regions["Marshal Barracks"]
    for MB_ID in ALL_MB:
        loc = ParadiseKillerLocation(world.player, MB_ID_TO_NAME[MB_ID], MB_ID, MB_region)
        MB_region.locations.append(loc)

    # Mountain Gorge
    MG_region = regions["Mountain Gorge"]
    for MG_ID in ALL_MG:
        loc = ParadiseKillerLocation(world.player, MG_ID_TO_NAME[MG_ID], MG_ID, MG_region)
        MG_region.locations.append(loc)

    # Opulent Ziggurat
    OZ_region = regions["Opulent Ziggurat"]
    for OZ_ID in ALL_OZ:
        loc = ParadiseKillerLocation(world.player, OZ_ID_TO_NAME[OZ_ID], OZ_ID, OZ_region)
        OZ_region.locations.append(loc)

    # Overworld
    O_region = regions["Overworld"]
    for O_ID in ALL_O:
        loc = ParadiseKillerLocation(world.player, O_ID_TO_NAME[O_ID], O_ID, O_region)
        O_region.locations.append(loc)

    # Paradise Gates
    PG_region = regions["Paradise Gates"]
    for PG_ID in ALL_PG:
        loc = ParadiseKillerLocation(world.player, PG_ID_TO_NAME[PG_ID], PG_ID, PG_region)
        PG_region.locations.append(loc)

    # Pyramid
    P_region = regions["Pyramid"]
    for P_ID in ALL_P:
        loc = ParadiseKillerLocation(world.player, P_ID_TO_NAME[P_ID], P_ID, P_region)
        P_region.locations.append(loc)

    # Reality Folding Drive
    RFD_region = regions["Reality Folding Drive"]
    for RFD_ID in ALL_RFD:
        loc = ParadiseKillerLocation(world.player, RFD_ID_TO_NAME[RFD_ID], RFD_ID, RFD_region)
        RFD_region.locations.append(loc)

    # Secret Bunker
    SB_region = regions["Secret Bunker"]
    for SB_ID in ALL_SB:
        loc = ParadiseKillerLocation(world.player, SB_ID_TO_NAME[SB_ID], SB_ID, SB_region)
        SB_region.locations.append(loc)

    # Secret Corridor
    SC_region = regions["Secret Corridor"]
    for SC_ID in ALL_SC:
        loc = ParadiseKillerLocation(world.player, SC_ID_TO_NAME[SC_ID], SC_ID, SC_region)
        SC_region.locations.append(loc)

    # Syndicate Apartments
    SA_region = regions["Syndicate Apartments"]
    for SA_ID in ALL_SA:
        loc = ParadiseKillerLocation(world.player, SA_ID_TO_NAME[SA_ID], SA_ID, SA_region)
        SA_region.locations.append(loc)

    # Syndicate Graveyard
    SG_region = regions["Syndicate Graveyard"]
    for SG_ID in ALL_SG:
        loc = ParadiseKillerLocation(world.player, SG_ID_TO_NAME[SG_ID], SG_ID, SG_region)
        SG_region.locations.append(loc)

    # Syndicate HQ
    SHQ_region = regions["Syndicate HQ"]
    for SHQ_ID in ALL_SHQ:
        loc = ParadiseKillerLocation(world.player, SHQ_ID_TO_NAME[SHQ_ID], SHQ_ID, SHQ_region)
        SHQ_region.locations.append(loc)

    # Tunnel
    T_region = regions["Tunnel"]
    for T_ID in ALL_T:
        loc = ParadiseKillerLocation(world.player, T_ID_TO_NAME[T_ID], T_ID, T_region)
        T_region.locations.append(loc)
    '''