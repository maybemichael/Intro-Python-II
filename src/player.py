# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, player_inventory = []):
        self.name = name
        self.current_room = current_room
        self.player_inventory = player_inventory

    def __str__(self):
        return f"{self.name} {self.current_room}"

    def move_player(user_input):
        user_input.lower()
        if user_input == "n":
            print("moving north")