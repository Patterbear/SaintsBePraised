# Move class
class Move(object):
    def __init__(self, move_id, category, title, cost, description, strength):
        self.move_id = move_id
        self.category = category
        self.title = title
        self.cost = cost
        self.description = description
        self.strength = strength

