from colorama import Fore

commands = [
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


def print_commands():
    for c in commands:
        print(Fore.GREEN, f"{c['description']} ({c['control']})")
