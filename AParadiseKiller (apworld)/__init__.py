from typing import ClassVar, Dict, Mapping, Any

from BaseClasses import Tutorial, ItemClassification as ItemClass, Item
from worlds.AutoWorld import World, WebWorld

from .Options import ParadiseKillerOptions, OptionGroup
from .Groups import item_name_groups, location_name_groups

from .Items import ParadiseKillerItem
from . import Locations, Regions, Rules, Options


class ParadiseKillerWeb(WebWorld):
    theme = "jungle"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Paradise Killer for Archipelago multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Caffeinated Moth"]
    )
    option_groups = [
        OptionGroup("Goal requirements", [
            Options.Goal,
            Options.NumberSodaCans,
            Options.NumberWhiskyBottles,
            Options.NumberRelationships,
            Options.MaxLevelRelationships
        ]),
        OptionGroup("Deathlink", [
            Options.DeathLink
        ]),
        OptionGroup("Gameplay", [
            Options.EnableNebulaDrinks,
            Options.EnableWhiskyBottles,
            Options.EnableShinjiLocations,
            Options.EnableStarlightSkins,
            Options.EnableIslandMomentos,
            Options.EnableMusicTracks,
            Options.EnableShrines,
            Options.EnableRecordings,
            Options.EnableRelationships
        ]),
        OptionGroup("Sphere Inhibitors", [
            Options.EnableSodaLicense,
            Options.EnableAlcoholLicense,
            Options.EnableDemonTranslator,
            Options.EnableMappingRequirement
        ]),
    ]


class ParadiseKillerWorld(World):
    game = "Paradise Killer"
    web = ParadiseKillerWeb()

    options_dataclass = ParadiseKillerOptions
    options: ParadiseKillerOptions

    item_name_to_id: ClassVar[Dict[str, int]] = Items.get_item_dict()
    item_id_to_name: ClassVar[Dict[int, str]] = {item_id: name for name, item_id in item_name_to_id.items()}
    # print(item_id_to_name)
    
    location_name_to_id: ClassVar[Dict[str, int]] = Locations.get_location_dict()
    location_id_to_name: ClassVar[Dict[int, str]] = {location_id: name for name, location_id in location_name_to_id.items()}
    # print(location_id_to_name)
    
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    def create_regions(self) -> None:
        regions = Regions.create_regions(self, self.options)
        Locations.create_locations(self, regions, self.options)
        self.multiworld.regions.extend(regions.values())

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        return ParadiseKillerItem(name, ItemClass.progression, item_id, self.player)

    def create_items(self) -> None:
        Items.populate_item_pool(self, self.options)

    def get_filler_item_name(self) -> str:
        return "Blood Crystal"

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {
            "goal":                         self.options.goal.value,
            "number_nebula_drinks":         self.options.number_nebula_drinks.value,
            "number_whisky_bottles":        self.options.number_whisky_bottles.value,
            "death_link":                   self.options.death_link.value,
            "enable_nebula_drinks":         self.options.enable_nebula_drinks.value,
            "enable_whisky_bottles":        self.options.enable_whisky_bottles.value,
            "enable_shinji_locations":      self.options.enable_shinji_locations.value,
            "enable_starlight_skins":       self.options.enable_starlight_skins.value,
            "enable_island_momentos":       self.options.enable_island_momentos.value,
            "enable_music_tracks":          self.options.enable_music_tracks.value,
            "enable_shrines":               self.options.enable_shrines.value,
            "enable_recordings":            self.options.enable_recordings.value,
            "enable_relationships":         self.options.enable_relationships.value,
            "enable_alcohol_license":       self.options.enable_alcohol_license.value,
            "enable_soda_license":          self.options.enable_soda_license.value,
            "enable_demon_translator":      self.options.enable_demon_translator.value,
            "enable_mapping_requirements":  self.options.enable_mapping_requirements.value,
        }
        return slot_data

    def set_rules(self) -> None:
        Rules.set_rules(self.multiworld, self, self.player, self.options)