
from .ItemLists.NebulaSoda import *
from .ItemLists.Whisky import *
from .LocationLists.Areas import *

item_name_groups ={
    "Nebula Soda Cans":         list(SODA_ID_TO_NAME.values()),
    "Whisky Bottles":           list(WHISKY_ID_TO_NAME.values())
}
location_name_groups = {
    "Idle Lands":               [name for name in IL_ID_TO_NAME.values()],
    "Agri Fields":              [name for name in AF_ID_TO_NAME.values()],
    "Beach":                    [name for name in B_ID_TO_NAME.values()],
    "Citizen Apartments":       [name for name in CA_ID_TO_NAME.values()],
    "Citizen Housing":          [name for name in CH_ID_TO_NAME.values()],
    "Council Building":         [name for name in CB_ID_TO_NAME.values()],
    "Court House":              [name for name in CH_ID_TO_NAME.values()],
    "Danchi":                   [name for name in D_ID_TO_NAME.values()],
    "Dead Zone":                [name for name in DZ_ID_TO_NAME.values()],
    "Deep Factory Entrance":    [name for name in DFE_ID_TO_NAME.values()],
    "Desolation Cell":          [name for name in DS_ID_TO_NAME.values()],
    "Doom Jazz's Yacht":        [name for name in DJY_ID_TO_NAME.values()],
    "Gardens":                  [name for name in G_ID_TO_NAME.values()],
    "K. HX's Workshop":         [name for name in KHX_ID_TO_NAME.values()],
    "Marshal Barracks":         [name for name in MB_ID_TO_NAME.values()],
    "Mountain Gorge":           [name for name in MG_ID_TO_NAME.values()],
    "Opulent Ziggurat":         [name for name in OZ_ID_TO_NAME.values()],
    "Overworld":                [name for name in O_ID_TO_NAME.values()],
    "Paradise Gates":           [name for name in PG_ID_TO_NAME.values()],
    "Pyramid":                  [name for name in P_ID_TO_NAME.values()],
    "Reality Folding Drive":    [name for name in RFD_ID_TO_NAME.values()],
    "Secret Bunker":            [name for name in SB_ID_TO_NAME.values()],
    "Secret Corridor":          [name for name in SC_ID_TO_NAME.values()],
    "Syndicate Apartments":     [name for name in SA_ID_TO_NAME.values()],
    "Syndicate Graveyard":      [name for name in SG_ID_TO_NAME.values()],
    "Syndicate HQ":             [name for name in SHQ_ID_TO_NAME.values()],
    "Tunnel":                   [name for name in T_ID_TO_NAME.values()],
}