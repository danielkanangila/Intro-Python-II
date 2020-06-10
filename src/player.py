# Write a class to hold player information, e.g. what room they are in
# currently.
from utils import *
from action import Action


class Player(Action):
    def __init__(self, name, current_room):
        super()
        self.name = name
        self.current_room = current_room

    def __str__(self):
        output = f"Name: {self.name}:\n\n"
        i = 1
        for item in self.items:
            output += f"\t{i}. {item.name}: {item.description}\n"
            i += 1

        return output

    def is_moving(self, action):
        c_action = list(
            filter(lambda item: item["control"] == action, move_controls))
        return False if not c_action else True

    def on_get(self, item_name):
        item = self.current_room.get_item(item_name)

        if not item:
            raise AttributeError(f"Item {item_name} does not exists.")

        self.current_room.remove_item(item_name)
        self.add_item(item)

    def on_drop(self, item_name):
        item = self.get_item(item_name)

        if not item:
            raise AttributeError(f"Item {item_name} does not exists.")

        self.remove_item(item_name)
        self.current_room.add_item(item)
