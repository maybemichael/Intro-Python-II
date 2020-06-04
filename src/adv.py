from room import Room
from player import Player
from item import Item
from game_helpers import GameHelpers


logo = """
     _______  _______  _______  _______ _________ _______             _______  ______            _______  _       _________          _______  _______
    (  ____ \(  ___  )(       )(       )\__   __/(  ____ \|\     /|  (  ___  )(  __  \ |\     /|(  ____ \( (    /|\__   __/|\     /|(  ____ )(  ____ \ 
    | (    \/| (   ) || () () || () () |   ) (   | (    \/| )   ( |  | (   ) || (  \  )| )   ( || (    \/|  \  ( |   ) (   | )   ( || (    )|| (    \/
    | (_____ | (___) || || || || || || |   | |   | |      | (___) |  | (___) || |   ) || |   | || (__    |   \ | |   | |   | |   | || (____)|| (__    
    (_____  )|  ___  || |(_)| || |(_)| |   | |   | |      |  ___  |  |  ___  || |   | |( (   ) )|  __)   | (\ \) |   | |   | |   | ||     __)|  __)   
          ) || (   ) || |   | || |   | |   | |   | |      | (   ) |  | (   ) || |   ) | \ \_/ / | (      | | \   |   | |   | |   | || (\ (   | (      
    /\____) || )   ( || )   ( || )   ( |___) (___| (____/\| )   ( |  | )   ( || (__/  )  \   /  | (____/\| )  \  |   | |   | (___) || ) \ \__| (____/\ 
    \_______)|/     \||/     \||/     \|\_______/(_______/|/     \|  |/     \|(______/    \_/   (_______/|/    )_)   )_(   (_______)|/   \__/(_______/                                                                                                                                                
"""

logo2 = """
       _____                           _      __       ___       __                 __                
      / ___/____ _____ ___  ____ ___  (______/ /_     /   | ____/ _   _____  ____  / /___  __________
      \__ \/ __ `/ __ `__ \/ __ `__ \/ / ___/ __ \   / /| |/ __  | | / / _ \/ __ \/ __/ / / / ___/ _ \ 
     ___/ / /_/ / / / / / / / / / / / / /__/ / / /  / ___ / /_/ /| |/ /  __/ / / / /_/ /_/ / /  /  __/ 
    /____/\__,_/_/ /_/ /_/_/ /_/ /_/_/\___/_/ /_/  /_/  |_\__,_/ |___/\___/_/ /_/\__/\__,_/_/   \___/                                                                                              
"""                                                                                                
print("   _____                           _      __       ___       __                 __                 ")
print("  / ___/____ _____ ___  ____ ___  (______/ /_     /   | ____/ _   _____  ____  / /___  __________  ")
print("  \__ \/ __ `/ __ `__ \/ __ `__ \/ / ___/ __ \   / /| |/ __  | | / / _ \/ __ \/ __/ / / / ___/ _ \ ")
print(" ___/ / /_/ / / / / / / / / / / / / /__/ / / /  / ___ / /_/ /| |/ /  __/ / / / /_/ /_/ / /  /  __/ ")
print("/____/\__,_/_/ /_/ /_/_/ /_/ /_/_/\___/_/ /_/  /_/  |_\__,_/ |___/\___/_/ /_/\__/\__,_/_/   \___/  ")

# Declare all the rooms
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

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

valid_input = ["y", "n"]
GameHelpers.start_game(valid_input)
text = ["\nHey stranger, what's your name?"]
GameHelpers.slow_type(text)
player_name = input(">")
# Make a new player object that is currently in the 'outside' room.
player = Player(player_name, room["outside"])
text = [f"You look famished {player.name}, are you up for an adventure to satisfy your munchies?"]
GameHelpers.slow_type(text)

print("[Y] Yes or [N]? ")
user_input = input(">")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
