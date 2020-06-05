# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, room_name, room_description, items=[], n_to=None, s_to=None, e_to=None, w_to=None):
        self.room_name = room_name
        self.room_description = room_description
        self.items = items
        self.connections = {
            "n": n_to,
            "s": s_to,
            "e": e_to,
            "w": w_to
        }

    def __str__(self):
        return f"Now in the{self.room_name}. {self.room_description}"
