import time
from colorama import Fore


class Trap:
    def __init__(self, player):
        self.player = player

    def trapped(self):
        attempt = 3
        while attempt:
            print(Fore.GREEN, f"\n{self.player.current_room}\n")
            #mins, secs = divmod(attempt, 60)
            print(Fore.YELLOW, f"You have {attempt} attempt left.")
            # time.sleep(1)

            choice = input("\n(n) North, (s) South, (e) East, (w) West \n")

            if self.player.is_moving(choice):
                current_room = self.player.current_room.get_next_room(choice)

                if current_room == None:
                    print(Fore.YELLOW, "\nThere is no room in this direction")
                else:
                    return current_room
            else:
                print(Fore.RED, f"\nInvalid action")

            attempt -= 1

        return "timeout"
