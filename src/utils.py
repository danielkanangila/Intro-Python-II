from colorama import Fore

move_controls = [
    {
        "control": "n",
        "description": "Move to North"
    },
    {
        "control": "s",
        "description": "Move to South"
    },
    {
        "control": "e",
        "description": "Move to East"
    },
    {
        "control": "w",
        "description": "Move to West"
    },
]

get_controls = [
    {
        "control": "get :item name",
        "description": "Get item"
    },
    {
        "control": "drop :item name",
        "description": "Drop item"
    },
]

help_controls = [
    {
        "control": "h",
        "description": "Help"
    },
    {
        "control": "i or inventory",
        "description": "Show player inventories"
    },
]

commands = move_controls + get_controls + help_controls


def print_commands():
    print("\nHelp")
    print("=====")
    for c in commands:
        print(Fore.GREEN, f"({c['control']}) {c['description']}")
