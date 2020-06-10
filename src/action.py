class Action:

    items = []

    def __init__(self, items=[]):
        self.items = items

    def get_item(self, item_name):
        return list(filter(lambda item: getattr(item, "name") == item_name, self.items))

    def remove_item(self, item_name):
        self.items = list(
            filter(lambda item: getattr(item, "name") != item_name, self.items))

    def add_item(self, item):
        self.items.append(*item)
