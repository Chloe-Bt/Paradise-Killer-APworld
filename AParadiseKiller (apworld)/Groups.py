
from .ItemLists.NebulaSodas import *
from .ItemLists.Whiskys import *
from .ItemLists.Keys import *
from .ItemLists.Upgrades import *
from .ItemLists.BloodCrystals import *
from .ItemLists.Crests import *
from .ItemLists.IslandMomentos import *
from .ItemLists.Carvings import *
from .ItemLists.Recordings import *
from .ItemLists.StarlightSkins import *
from .ItemLists.KeyItems import *
from .ItemLists.Relics import *

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
from .LocationLists.SecretCorridor import *
from .LocationLists.SyndicateApartments import *
from .LocationLists.SyndicateGraveyard import *
from .LocationLists.SyndicateHQ import *
from .LocationLists.Tunnel import *

item_name_groups = {
    "Upgrades":                 set(WHISKY_ID_TO_NAME.values()),
    "Sphere Keys":              set(KEY_ID_TO_NAME.values()),
    "Blood Crystals":           set(BC_ID_TO_NAME.values()),
    "Nebula Soda Drinks":       set(SODA_ID_TO_NAME.values()),
    "Whisky Bottles":           set(WHISKY_ID_TO_NAME.values()),
    "Crests":                   set(CREST_ID_TO_NAME.values()),
    "Island Momentos":          set(IM_ID_TO_NAME.values()),
    "Carvings":                 set(CARVING_ID_TO_NAME.values()),
    "Recordings":               set(RECORDING_ID_TO_NAME.values()),
    "Starlight Skins":          set(STARLIGHTS_ID_TO_NAME.values()),
    "Key Items":                set(KI_ID_TO_NAME.values()),
    "Relics":                   set(RELIC_ID_TO_NAME.values()),
}

location_name_groups = {
    "Idle Lands":               set(IL_ID_TO_NAME.values()),
    "Agri Fields":              set(AF_ID_TO_NAME.values()),
    "Dead Zone":                set(DZ_ID_TO_NAME.values()),
    "Beach":                    set(B_ID_TO_NAME.values()),
    "Citizen Apartments":       set(CA_ID_TO_NAME.values()),
    "Citizen Housing":          set(CH_ID_TO_NAME.values()),
    "Council Building":         set(CB_ID_TO_NAME.values()),
    "Court House":              set(CH_ID_TO_NAME.values()),
    "Danchi":                   set(D_ID_TO_NAME.values()),
    "Deep Factory Entrance":    set(DFE_ID_TO_NAME.values()),
    "Desolation Cell":          set(DC_ID_TO_NAME.values()),
    "Doom Jazz's Yacht":        set(DJY_ID_TO_NAME.values()),
    "Gardens":                  set(G_ID_TO_NAME.values()),
    "K. HX's Workshop":         set(KHX_ID_TO_NAME.values()),
    "Marshal Barracks":         set(MB_ID_TO_NAME.values()),
    "Mountain Gorge":           set(MG_ID_TO_NAME.values()),
    "Opulent Ziggurat":         set(OZ_ID_TO_NAME.values()),
    "Overworld":                set(O_ID_TO_NAME.values()),
    "Paradise Gates":           set(PG_ID_TO_NAME.values()),
    "Pyramid":                  set(P_ID_TO_NAME.values()),
    "Reality Folding Drive":    set(RFD_ID_TO_NAME.values()),
    "Secret Corridor":          set(SC_ID_TO_NAME.values()),
    "Syndicate Apartments":     set(SA_ID_TO_NAME.values()),
    "Syndicate Graveyard":      set(SG_ID_TO_NAME.values()),
    "Syndicate HQ":             set(SHQ_ID_TO_NAME.values()),
    "Tunnel":                   set(T_ID_TO_NAME.values()),
}