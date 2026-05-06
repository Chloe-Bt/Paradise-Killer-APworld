from BaseClasses import MultiWorld, CollectionState

from . import Items, ParadiseKillerOptions
from ..generic.Rules import add_rule

def set_rules(multiworld: MultiWorld, world, player: int, options: ParadiseKillerOptions):
    set_goal(multiworld, world, player, options)


def set_goal(multiworld: MultiWorld, world, player: int, options: ParadiseKillerOptions):
    multiworld.completion_condition[player] = lambda state: (
        state.has("Starlight Upgrade: Pyramids", player)
    )
    '''
    match options.goal.value:
        case options.goal.option_lady_soda_dies:
            multiworld.completion_condition[player] = lambda state: (
                state.has_group("Nebula Soda Drinks", player, options.number_nebula_drinks.value)
            )
        case options.goal.option_lady_whisky_dies:
            multiworld.completion_condition[player] = lambda state: (
                state.has_group("Whisky Bottles", player, options.number_whisky_bottles.value)
            )
    '''