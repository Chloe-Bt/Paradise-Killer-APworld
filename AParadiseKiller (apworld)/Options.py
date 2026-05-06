from dataclasses import dataclass
from random import choice

from Options import PerGameCommonOptions, DeathLink, Choice, Toggle, OptionGroup, Range, StartInventoryPool

#Goals
class Goal(Choice):
    """
    Choose your goal for the multiworld
    Lady Soda Dies: Get X amount of nebula soda drinks.
    Lady Whisky Dies: Get X amount of whisky bottles.
    Lady Love Dies: Get X relation level with Y amount of people.
    """
    display_name = "Goal"
    option_lady_soda_dies = 0
    option_lady_whisky_dies = 1
    option_lady_love_dies = 2
    default = option_lady_soda_dies

class NumberSodaCans(Range):
    """
    Only applicable if your goal is set to 'Lady Soda Dies'.
    How many Nebula Drinks to find before winning your game.
    """
    display_name = "Number of Nebula Soda cans"
    range_start = 1
    range_end = 23
    default = 12

class NumberWhiskyBottles(Range):
    """
    Only applicable if your goal is set to 'Lady Whisky Dies'.
    How many Whisky Drinks to find before winning your game.
    """
    display_name = "Number of Whisky Bottles"
    range_start = 1
    range_end = 13
    default = 7
class NumberRelationships(Range):
    """
    Only applicable if your goal is set to 'Lady Love Dies'.
    How many Relationships to max before winning your game.
    """
    display_name = "Number of maxed relationships"
    range_start = 1
    range_end = 10
    default = 5

class MaxLevelRelationships(Range):
    """
    Only applicable if your goal is set to 'Lady Love Dies'.
    What level do your your relationship to be before being considered for the win condition.
    """
    display_name = "Maximum level relationships"
    range_start = 1
    range_end = 5
    default = 3



#Randomizer settings
class EnableNebulaDrinks(Toggle):
    """
    Enable Nebula Soda Drinks as items and locations.
    """
    display_name = "Enable Nebula Soda Drinks"
    default: 1

class EnableWhiskyBottles(Toggle):
    """
    Enable Whisky Bottles as items and locations.
    """
    display_name = "Enable Whisky Bottles"
    default: 1

class EnableShinjiLocations(Toggle):
    """
    Enable Shinji locations in the game world.
    """
    display_name = "Enable Shinji Locations"
    default: 1

class EnableStarlightSkins(Toggle):
    """
    Enable Starlight skins as items and locations.
    """
    display_name = "Enable Starlight Skins"
    default: 1

class EnableIslandMomentos(Toggle):
    """
    Enable Island Mementos as items and locations.
    """
    display_name = "Enable Island Momentos"
    default: 1

class EnableMusicTracks(Toggle):
    """
    Enable in-game music tracks as items and locations.
    """
    display_name = "Enable Music Tracks"
    default: 1

class EnableShrines(Toggle):
    """
    Enable shrines as items and locations.
    """
    display_name = "Enable Shrines"
    default: 1

class EnableRecordings(Toggle):
    """
    Enable collectible recordings as items and locations.
    """
    display_name = "Enable Recordings"
    default: 1

class EnableRelationships(Toggle):
    """
    Enable character relationship mechanics in the game.
    """
    display_name = "Enable Relationships"
    default: 1



#Sphere limiters
class EnableAlcoholLicense(Toggle):
    """
    Enables a required key item before you are able to get checks from Whisky Bottles
    """
    display_name = "Enable Alcohol License"
    default: 1

class EnableSodaLicense(Toggle):
    """
    Enables a required key item before you are able to get checks from the Nebula Drink vending machines.
    """
    display_name = "Enable Soda License"
    default: 1

class EnableDemonTranslator(Toggle):
    """
    Enables a required key item before you are able to get checks from talking to Sjinji.
    """
    display_name = "Enable Demon Translator"
    default: 1

class EnableMusicPlayer(Toggle):
    """
    Enables a require key item before you are able to get checks from the broadcasting towers on the island.
    """
    display_name = "Enable Music Player:"
    default: 1

class EnableMappingRequirement(Toggle):
    """
    Enables a required key item from each main map location before you are able to acces that map area checks.",
    Highly recommended to turn it on to prevent massive early spheres.
    """
    display_name = "Enable Mapping Requirement:"
    default: 1



@dataclass
class ParadiseKillerOptions(PerGameCommonOptions):
    goal: Goal
    number_nebula_drinks: NumberSodaCans
    number_whisky_bottles: NumberWhiskyBottles
    number_max_relationships: NumberRelationships
    max_lvl_relationship: MaxLevelRelationships

    enable_nebula_drinks: EnableNebulaDrinks
    enable_whisky_bottles: EnableWhiskyBottles
    enables_shinji_locations: EnableShinjiLocations
    enable_starlight_skins: EnableStarlightSkins
    enable_island_momentos: EnableIslandMomentos
    enable_music_tracks: EnableMusicTracks
    enable_shrines: EnableShrines
    enable_recordings: EnableRecordings
    enable_relationships: EnableRelationships

    enable_alcohol_license: EnableSodaLicense
    enable_soda_license: EnableAlcoholLicense
    enable_music_player: EnableMusicPlayer
    enable_demon_translator: EnableDemonTranslator
    enable_mapping_requirements: EnableMappingRequirement