import sys
import time
from room import Room
from player import Player
# from item import Item
from game_helpers import GameHelpers


# print("   _____                           _      __       ___       __                 __                 ")
# print("  / ___/____ _____ ___  ____ ___  (______/ /_     /   | ____/ _   _____  ____  / /___  __________  ")
# print("  \__ \/ __ `/ __ `__ \/ __ `__ \/ / ___/ __ \   / /| |/ __  | | / / _ \/ __ \/ __/ / / / ___/ _ \ ")
# print(" ___/ / /_/ / / / / / / / / / / / / /__/ / / /  / ___ / /_/ /| |/ /  __/ / / / /_/ /_/ / /  /  __/ ")
# print("/____/\__,_/_/ /_/ /_/_/ /_/ /_/_/\___/_/ /_/  /_/  |_\__,_/ |___/\___/_/ /_/\__/\__,_/_/   \___/  ")

# Properties
directions = ["n", "s", "e", "w", "q"]
playing = False
outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons")
foyer = Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.")
overlook = Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.")
narrow = Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.")
treasure = Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.")


room = {
    'outside': outside,
    'foyer': foyer,
    'overlook': overlook,
    'narrow': narrow,
    'treasure': treasure,
}

current = set()

# Link rooms together

room['outside'].connections["n"] = room['foyer']
room['foyer'].connections["s"] = room['outside']
room['foyer'].connections["n"] = room['overlook']
room['foyer'].connections["e"] = room['narrow']
room['overlook'].connections["s"] = room['foyer']
room['narrow'].connections["w"] = room['foyer']
room['narrow'].connections["n"] = room['treasure']
room['treasure'].connections["s"] = room['narrow']

#
# Main
#

# Write a loop that:

user_choice = GameHelpers.prompt_to_play()
GameHelpers.play(user_choice)
playing = GameHelpers.is_playing
player_name = GameHelpers.create_player()
player = Player(player_name, room["outside"])
if playing:
    print("\n")
else:
    time.sleep(2.5)
    sys.exit()

while playing:
    time.sleep(1.5)
    GameHelpers.munchies_random()
    print(f"\n{player.current_room}\n")
    GameHelpers.munchies_speaks("Where would you like to go?\n")
    print("\nPlease Choose a direction, press [N] for North, [S] for South, [E] for East, [W] for West")
    user_choice = GameHelpers.is_choice_valid(directions)
    player.move_player(user_choice)
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
