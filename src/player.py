# Write a class to hold player information, e.g. what room they are in
# currently.
from game_helpers import GameHelpers
import time


class Player:


    def __init__(self, name, current_room, player_inventory=[]):
        self.name = name
        self.current_room = current_room
        self.player_inventory = player_inventory

    def __str__(self):
        return f"{self.name} {self.current_room}"

    def move_player(self, direction: str):
        north_room = self.current_room.connections["n"]
        south_room = self.current_room.connections["s"]
        east_room = self.current_room.connections["e"]
        west_room = self.current_room.connections["w"]
        all_rooms = [north_room, south_room, east_room, west_room]
        connecting_rooms = [room for room in all_rooms if room is not None]
        if direction == "n":
            if self.current_room.connections["n"] is not None:
                self.current_room = self.current_room.connections["n"]
            else:
                GameHelpers.munchies_speaks("Uhh... buddy, there is no way through this wall...\n")
                GameHelpers.munchies_speaks("Open your eyes man...\n")
                for room in connecting_rooms:
                    if room is south_room:
                        GameHelpers.munchies_speaks(f"We can go South to the {south_room.room_name}\n")
                    if room is east_room:
                        GameHelpers.munchies_speaks(f"We can go East to the {east_room.room_name}\n")
                    if room is west_room:
                        GameHelpers.munchies_speaks(f"We can go West to the {west_room.room_name}\n")
        elif direction == "s":
            if self.current_room.connections["s"] is not None:
                self.current_room = self.current_room.connections["s"]
            else:
                GameHelpers.munchies_speaks("Uhh... buddy, there is no way through this wall...\n")
                GameHelpers.munchies_speaks("Open your eyes man...\n")
                for room in connecting_rooms:
                    if room is north_room:
                        GameHelpers.munchies_speaks(f"We can go North to the {north_room.room_name}\n")
                    if room is east_room:
                        GameHelpers.munchies_speaks(f"We can go East to the {east_room.room_name}\n")
                    if room is west_room:
                        GameHelpers.munchies_speaks(f"We can go West to the {west_room.room_name}\n")
        elif direction == "e":
            if self.current_room.connections["e"] is not None:
                self.current_room = self.current_room.connections["e"]
            else:
                GameHelpers.munchies_speaks("Uhh... buddy, there is no way through this wall...\n")
                GameHelpers.munchies_speaks("Open your eyes man...\n")
                for room in connecting_rooms:
                    if room is north_room:
                        GameHelpers.munchies_speaks(f"We can go North to the {north_room.room_name}\n")
                    if room is south_room:
                        GameHelpers.munchies_speaks(f"We can go South to the {south_room.room_name}\n")
                    if room is west_room:
                        GameHelpers.munchies_speaks(f"We can go West to the {west_room.room_name}\n")
        elif direction == "w":
            if self.current_room.connections["w"] is not None:
                self.current_room = self.current_room.connections["w"]
            else:
                GameHelpers.munchies_speaks("Uhh... buddy, there is no way through this wall...\n")
                GameHelpers.munchies_speaks("Open your eyes man...\n")
                for room in connecting_rooms:
                    if room is north_room:
                        GameHelpers.munchies_speaks(f"We can go North to the {north_room.room_name}\n")
                    if room is south_room:
                        GameHelpers.munchies_speaks(f"We can go South to the {south_room.room_name}\n")
                    if room is east_room:
                        GameHelpers.munchies_speaks(f"We can go East to the {east_room.room_name}\n")

    def search_room(self):
        GameHelpers.type_out("Searching...")
        time.sleep(1)
        GameHelpers.munchies_speaks("Here is what I found...")
        for item in self.current_room.items:
            print(f"{item}", end=" ")


    def pickup_item(self, object_name: str):
        room_items = self.current_room.items
        item_array = [item for item in room_items if item.name is object_name]
        self.current_room.items.remove(object_name)
        if len(self.player_inventory) is 3:
            print("Unable to pick up item!\nYour inventory is full.")
            
        elif len(self.player_inventory) is 1:
            self.player_inventory = [item for item in room_items if item.name is object_name]
            print("Successfully added Item. Your inventory is 1 out of 3")
            self.player_inventory.append(item_array[0])
        elif len(self.player_inventory) is 2:
            print("Successfully added Item. Your inventory is 2 out of 3")
            self.player_inventory.append(item_array[0])

    def drop_item(self, object_name: str):
        item_array = [item for item in item if item.name is object_name]
        self.current_room.items.append(item_array)
        self.player_inventory.remove(object_name)