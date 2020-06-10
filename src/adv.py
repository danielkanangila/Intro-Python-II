import sys
from room import Room
from player import Player
from colorama import Fore
from utils import *
from item import Item
from pyfiglet import Figlet

table = Item("Table", "Tropical black wood table")
bag = Item("Backpack", "Tactical Army backpack")
knife = Item("Bayonet", "AK41 knife")
weapon1 = Item("Glock17", "Firearm")
weapon2 = Item("M16", "Firearm")
weapon3 = Item("M-14", "Firearm")
weapon4 = Item("UZI", "Firearm")
weapon5 = Item("AK-47", "Firearm")
drink = Item("Energy-Drink", "Energy Drink")

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [table, knife, bag]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [table, bag, drink, weapon1]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [weapon1, weapon5, ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [weapon1, weapon3, weapon1, drink]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [weapon1, weapon2, weapon3, weapon4, weapon5, drink, drink]),
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

# Make a new player object that is currently in the 'outside' room.
player = Player("player1", room['outside'])
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
f = Figlet(font="slant")
print(f.renderText("Welcome to Cave"))
print(Fore.GREEN, "\ntype (q) to quit, (h) for help\n")

while True:
    print(Fore.GREEN, f"\n{player.current_room}\n")
    choice = input("(n) North, (s) South, (e) East, (w) West \n(i) \
or (inventory) Inventory, (get :item name) Pick Item \
\n(drop : item name), (h) help, (q) quit: ")

    try:
        if choice == 'q':
            break
        if choice == 'h':
            print_commands()

        if player.is_moving(choice):
            key = f"{choice}_to"
            current_room = getattr(player.current_room, key)

            if current_room == None:
                print(Fore.YELLOW, "\nThere is no room in this direction")
            else:
                player.current_room = current_room

        if (choice == "i") | (choice == "inventory"):
            print(f"\n{player}")

        choice = choice.split(" ")

        if (len(choice) == 2) & (choice[0] == "get"):
            player.on_get(choice[1])

        if (len(choice) == 2) & (choice[0] == "drop"):
            player.on_drop(choice[1])

    except AttributeError as e:
        print(Fore.RED, f"\n{e}")
    except Exception as e:
        print(sys.exc_info())
        raise
