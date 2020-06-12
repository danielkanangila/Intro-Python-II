class Action:
    REACH_OUTSIDE_CAVE = "REACH_OUTSIDE_CAVE"
    REACH_FOYER = "REACH_FOYER"
    REACH_GRAND_OVERLOOK = "REACH_GRAND_OVERLOOK"
    REACH_NARROW_PASSAGE = "REACH_NARROW_PASSAGE"
    REACH_TRAPPED_PASSAGE = "REACH_TRAPPED_PASSAGE"
    REACH_TREASURE_CHAMBER = "REACH_TREASURE_CHAMBER"
    GET_SWORD = "GET_SWORD"
    GET_TREASURE = "GET_TREASURE"
    GET_ENERGY = "GET_ENERGY"
    GET_WEAPON = "GET_WEAPON"

    items = []

    def __init__(self, items=[]):
        self.items = items

    def get_item(self, item_name: str):
        return list(filter(lambda item: getattr(item, "name") == item_name, self.items))

    def remove_item(self, item_name: str):
        self.items = list(
            filter(lambda item: getattr(item, "name") != item_name, self.items))

    def add_item(self, item):
        self.items.append(*item)

    # return the correct action room name
    def get_action_by_name(self, room_name: str):
        if room_name == "Foyer":
            return self.REACH_FOYER
        if room_name == "Grand Overlook":
            return self.REACH_GRAND_OVERLOOK
        if room_name == "Narrow Passage":
            return self.REACH_NARROW_PASSAGE
        if room_name == "Trapped Passage":
            return self.REACH_TRAPPED_PASSAGE
        if room_name == "Treasure Chamber":
            return self.REACH_TREASURE_CHAMBER
