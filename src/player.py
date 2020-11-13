# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current):
        self.current = current
        self.holding = []

    def pick_item(self, item):
        self.holding.append(item)

    def drop_item(self, item):
        self.holding.remove(item)

    def player_holding(self):
        print(f"You are currently holding {len(self.holding)} items")
        for item in self.holding:
            print(item)
