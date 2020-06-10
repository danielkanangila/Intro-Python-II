# Implement a class to hold room information. This should have name and
# description attributes.
from action import Action


class Room(Action):
    def __init__(self, name, description, items=[]):
        super().__init__(items)
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        output = f"Welcome to {self.name}: \n{self.description}.\n\n"
        i = 1
        for item in self.items:
            output += f"\t{i}. {item.name}: {item.description}\n"
            i += 1

        return output
