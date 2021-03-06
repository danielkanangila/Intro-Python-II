import sys
from room import Room
from player import Player
from trap import Trap
from colorama import Fore
from utils import *
from item import Item
from pyfiglet import Figlet
from score import Score

table = Item("Table", "Tropical black wood table")
bag = Item("Backpack", "Tactical Army backpack")
knife = Item("Bayonet", "Legendary King's Arthur sword Excalibur")
sword = Item("Sword", "AK41 knife")
weapon1 = Item("Glock17", "Firearm")
weapon2 = Item("M16", "Firearm")
weapon3 = Item("M-14", "Firearm")
weapon4 = Item("UZI", "Firearm")
weapon5 = Item("AK-47", "Firearm")
drink = Item("Energy-Drink", "Energy Drink")
treasureChest = Item("Treasure", "Salmon Treasure")

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [table, knife, bag]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [table, bag, drink, weapon1]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [sword, weapon1, weapon5, weapon3]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [drink, drink]),
    'trap': Room("Trapped Passage", """The trapped passage which leads to the treasure room. 
You can only 3 attempt to escape to this room."""),
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
room['narrow'].e_to = room['trap']
room['trap'].w_to = room['narrow']
room['trap'].s_to = room['treasure']
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

# clean termina
print(chr(27) + "[2J")
f = Figlet(font="slant")
print(f.renderText("Welcome to Cave"))
print(Fore.GREEN, "\ntype (q) to quit, (h) for help\n")

# instantiate score
score = Score()

while True:
    print(Fore.GREEN, f"\n{player.current_room}\n")
    print(f"============= {score} =============")
    choice = input("(n) North, (s) South, (e) East, (w) West \n(i) \
or (inventory) Inventory, (get :item name) Pick Item \
\n(drop : item name), (h) help, (q) quit: ")

    try:
        if choice == 'q':
            break
        if choice == 'h':
            print_commands()

        # if choice equal to `n` | `s` | `e` | `w`
        if player.is_moving(choice):
            # get the nex room following the choice
            current_room = player.current_room.get_next_room(choice)
            # update score
            score.update(player)

            if current_room == None:
                print(Fore.YELLOW, "\nThere is no room in this direction")
            else:
                # update player current room
                player.change_room(current_room)

                # Trapped player if current room equal to trapped passage
                if player.current_room.name == "Trapped Passage":
                    print("\n\n")
                    trap = Trap(player)
                    res = trap.trapped()
                    if (res == "timeout"):
                        print(f.renderText("Game Over"))
                        break
                    else:
                        player.change_room(res)
        # Print player item inventories
        if (choice == "i") | (choice == "inventory"):
            print(f"\n{player}")

        # if input is `verb` `object`
        choice = choice.split(" ")

        # GET `item` action
        if (len(choice) == 2) & (choice[0] == "get"):
            player.on_get(choice[1])

        # DROP `item` action
        if (len(choice) == 2) & (choice[0] == "drop"):
            player.on_drop(choice[1])

    except AttributeError as e:
        print(Fore.RED, f"\n{e}")
    except Exception as e:
        print(sys.exc_info())
        raise
