class Node:
    def __init__(self, state, cost):
        self.state = state
        self.cost = cost
        self.visited = False

    def visit(self):
        self.visited = True
        return self.state
