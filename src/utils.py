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

commands = move_controls + get_controls


def print_commands():
    for c in commands:
        print(Fore.GREEN, f"{c['description']} ({c['control']})")
