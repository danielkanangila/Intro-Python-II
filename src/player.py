# Write a class to hold player information, e.g. what room they are in
# currently.
from utils import *
from action import Action
from room import Room


class Player(Action):

    # store player movement history
    trace = {}
    # the last player action
    last_action: str = ""
    current_room: Room = None

    def __init__(self, name, current_room: Room):
        super()
        self.name = name
        self.change_room(current_room)

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

    # update player movement hostory
    def update_trace(self, action: str):
        if action in self.trace:
            self.trace[action] = self.trace[action] + 1
        else:
            self.trace[action] = 1

    # change player current room and movement history
    def change_room(self, current_room: Room):
        # change current room
        self.current_room = current_room

        # update trace and last action
        action_name = self.get_action_by_name(current_room.name)
        self.last_action = action_name
        self.update_trace(action_name)
