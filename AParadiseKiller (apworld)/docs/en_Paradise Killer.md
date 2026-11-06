# Paradise Killer Archipelago

## What does randomization do to this Game?
- Shuffles nebula drinks, whiskey bottles, relics, key items, Starlight (upgrades), LLD upgrades away from their original items.

## What is the goal of Paradise Killer in Archipelago
The goal of Paradise Killer can be:
- Lady Soda Dies -	get X amount of nebula soda drinks send your way
- Lady Whisky Dies -	get X amount of whisky bottles send your way

Finishing any of these goals will immediately mark your game as complete, eventually this will be changed so that you are allowed to pick up the Investigator's Gun and finish the game with the trial.

## What other adjustments have been made to the base game?
- Sphere limiters are in place for each region as definied on the in-game map for the sole reason to prevent a massive sphere 1. These are currently just logic based, and as such require an instance of [universal tracker](https://github.com/FarisTheAncient/Archipelago/releases?q=Tracker) to be active on the side and are require an honor system.
  - Each game area (for example: Beach, Danchi, Opulent Ziggurat) has a seperate unlock item to be received from the multiworld.
  - Whisky License: allows you to pickup whisky bottles.
  - Soda License: allows you to interact with the Dead Nebula vending machines.
- The name of LLD in dialogue is changed to the name of the archipelago slot name.
- One of the Whisky Drinkers is named Moth.

## What does another world's item look like in Paradise Killer?
Items retain their original appearance. You won't know if an item is for another player until you collect it. Once collected they will still popup as if they are their original item, this is something that is yet to be fixed.

## In-Game Client Commands
You can use either the ~ or f10 key to bring up the in-game client. Press it twice to actually see the text client.
- `/connect {address:port} "{slotname}" "{password}"`
  - Used to connect to the multiworld. Password is optional
- `/disconnect`
  - Disconnect from the multiworld
- `/deathlink`
  - Toggles deathlink
- `/say or /message {message}`
  - Send a message to the archipelago chat
- `/blood {#number}`
  - Gives the player #number of blood crystals, in case of debugging.
- `/exile`
  - Teleport the player back to exile, in case the player forgot an item there during the intro sequence.
