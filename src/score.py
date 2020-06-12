from action import Action
from player import Player


class Score:
    action_score = {}

    current_score = 0

    def __init__(self):
        action = Action()
        self.action_score[action.REACH_OUTSIDE_CAVE] = 0
        self.action_score[action.REACH_FOYER] = 10
        self.action_score[action.REACH_GRAND_OVERLOOK] = 15
        self.action_score[action.REACH_NARROW_PASSAGE] = 30
        self.action_score[action.REACH_TRAPPED_PASSAGE] = 50
        self.action_score[action.REACH_TREASURE_CHAMBER] = 100
        self.action_score[action.GET_SWORD] = 100
        self.action_score[action.GET_TREASURE] = 10000
        self.action_score[action.GET_WEAPON] = 5

    def update(self, player: Player):
        action = player.last_action
        if (player.trace[action] == 1) & (action != None):
            self.current_score += self.action_score[action]

    def __str__(self):
        return f"Score: {self.current_score}"
