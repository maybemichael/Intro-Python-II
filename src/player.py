# Write a class to hold player information, e.g. what room they are in
# currently.
from game_helpers import GameHelpers


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
