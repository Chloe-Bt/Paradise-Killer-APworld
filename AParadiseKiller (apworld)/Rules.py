from BaseClasses import MultiWorld, CollectionState

from . import Items, ParadiseKillerOptions
from ..generic.Rules import add_rule

def set_rules(multiworld: MultiWorld, world, player: int, options: ParadiseKillerOptions):
    set_goal(multiworld, world, player, options)


def set_goal(multiworld: MultiWorld, world, player: int, options: ParadiseKillerOptions):
    match options.goal.value:
        case options.goal.option_lady_soda_dies:
            multiworld.completion_condition[player] = lambda state: (
                state.has_group("Nebula Soda Drinks", player, options.number_nebula_drinks.value)
            )
        case options.goal.option_lady_whisky_dies:
            multiworld.completion_condition[player] = lambda state: (
                state.has_group("Whisky Bottles", player, options.number_whisky_bottles.value)
            )
        case options.goal.option_lady_love_dies:
            multiworld.completion_condition[player] = lambda state: (
                has_required_relationships(state, world, player)
            )

def has_required_relationships(state, world, player):
    count = 0

    required_count = world.options.number_max_relationships.value
    required_level = world.options.max_lvl_relationship.value

    relationship_items = [
        "Progressive Grand Marshal Akiko 14 Relationship",
        "Progressive Carmelina Silence Relationship",
        "Progressive Crimson Acid Relationship",
        "Progressive Henry Division Relationship",
        "Progressive Lydia Day Break Relationship",
        "Progressive Doctor Doom Jazz Relationship",
        "Progressive Sam Day Break Relationship",
        "Progressive The Witness To The End Relationship",
        "Progressive Yuri Night Relationship",
        "Progressive One Last Kiss Relationship",
    ]

    for item in relationship_items:
        if state.count(item, player) >= required_level:
            count += 1
    return count >= required_count