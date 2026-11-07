from dataclasses import dataclass
from random import choice
from Options import PerGameCommonOptions, DeathLink, Choice, Visibility, Toggle, DefaultOnToggle, OptionGroup, Range, StartInventoryPool

# Goal Settings
class Goal(Choice):
    """
    Lady Soda Dies: Get X amount of nebula soda drinks.
    Lady Whisky Dies: Get X amount of whisky bottles.
    Lady Love Dies: Get X relation level with Y amount of people.
    """
    display_name = "Goal"
    option_lady_soda_dies = 0
    option_lady_whisky_dies = 1
    default = option_lady_soda_dies

class NumberSodaCans(Range):
    """
    Only applicable if your goal is set to 'Lady Soda Dies'.
    How many Nebula Drinks to find before winning your game.
    """
    display_name = "Number of Nebula Soda cans"
    range_start = 1
    range_end = 23
    default = 17

class NumberWhiskyBottles(Range):
    """
    Only applicable if your goal is set to 'Lady Whisky Dies'.
    How many Whisky Drinks to find before winning your game.
    """
    display_name = "Number of Whisky Bottles"
    range_start = 1
    range_end = 13
    default = 10

class NumberRelationships(Range):
    """
    Only applicable if your goal is set to 'Lady Love Dies'.
    How many Relationships to max before winning your game.
    """
    display_name = "Number of maxed relationships"
    range_start = 1
    range_end = 10
    default = 5
    visibility = Visibility.none

class MaxLevelRelationships(Range):
    """
    Only applicable if your goal is set to 'Lady Love Dies'.
    What level do your your relationship to be before being considered for the win condition.
    """
    display_name = "Maximum level relationships"
    range_start = 1
    range_end = 5
    default = 3
    visibility = Visibility.none



# Randomizer Settings
class EnableNebulaDrinks(DefaultOnToggle):
    """
    Enable Nebula Soda Drinks as items and locations.
    """
    display_name = "Enable Nebula Soda Drinks"

class EnableWhiskyBottles(DefaultOnToggle):
    """
    Enable Whisky Bottles as items and locations.
    """
    display_name = "Enable Whisky Bottles"

class EnableShinjiLocations(Toggle):
    """
    Enable Shinji locations in the game world.
    """
    display_name = "Enable Shinji Locations"
    visibility = Visibility.none

class EnableStarlightSkins(DefaultOnToggle):
    """
    Enable Starlight skins as items and locations.
    """
    display_name = "Enable Starlight Skins"

class EnableIslandMomentos(DefaultOnToggle):
    """
    Enable Island Mementos as items and locations.
    """
    display_name = "Enable Island Momentos"

class EnableMusicTracks(DefaultOnToggle):
    """
    Enable in-game music tracks as items and locations.
    """
    display_name = "Enable Music Tracks"

class EnableShrines(DefaultOnToggle):
    """
    Enable shrines as items and locations.
    """
    display_name = "Enable Shrines"

class EnableRecordings(DefaultOnToggle):
    """
    Enable collectible recordings as items and locations.
    """
    display_name = "Enable Recordings"
    
class EnableRelationships(Toggle):
    """
    Enable character relationship mechanics in the game.
    """
    display_name = "Enable Relationships"
    visibility = Visibility.none



#Sphere Limiters
class EnableAlcoholLicense(DefaultOnToggle):
    """
    Enables a required key item before you are able to get checks from Whisky Bottles
    """
    display_name = "Enable Alcohol License"
    default: 1

class EnableSodaLicense(DefaultOnToggle):
    """
    Enables a required key item before you are able to get checks from the Nebula Drink vending machines.
    """
    display_name = "Enable Soda License"

class EnableDemonTranslator(Toggle):
    """
    Enables a required key item before you are able to get checks from talking to Sjinji.
    """
    display_name = "Enable Demon Translator"
    visibility = Visibility.none

class EnableMusicPlayer(DefaultOnToggle):
    """
    Enables a require key item before you are able to get checks from the broadcasting towers on the island.
    """
    display_name = "Enable Music Player:"

class EnableMappingRequirement(DefaultOnToggle):
    """
    Enables a required key item from each main map location before you are able to acces that map area checks.",
    Highly recommended to turn it on to prevent massive early spheres.
    """
    display_name = "Enable Mapping Requirement:"



@dataclass
class ParadiseKillerOptions(PerGameCommonOptions):
    goal:                        Goal
    number_nebula_drinks:        NumberSodaCans
    number_whisky_bottles:       NumberWhiskyBottles
    number_max_relationships:    NumberRelationships
    max_lvl_relationship:        MaxLevelRelationships
    
    death_link:                  DeathLink

    enable_nebula_drinks:        EnableNebulaDrinks
    enable_whisky_bottles:       EnableWhiskyBottles
    enable_shinji_locations:     EnableShinjiLocations
    enable_starlight_skins:      EnableStarlightSkins
    enable_island_momentos:      EnableIslandMomentos
    enable_music_tracks:         EnableMusicTracks
    enable_shrines:              EnableShrines
    enable_recordings:           EnableRecordings
    enable_relationships:        EnableRelationships
    
    enable_alcohol_license:      EnableSodaLicense
    enable_soda_license:         EnableAlcoholLicense
    enable_demon_translator:     EnableDemonTranslator
    enable_mapping_requirements: EnableMappingRequirement