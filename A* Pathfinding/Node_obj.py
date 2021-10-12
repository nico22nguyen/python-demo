class Node:
    def __init__(self, row, col, h_cost, parent):
        self.row = row
        self.col = col
        self.parent = parent
        self.h_cost = h_cost

    def g_cost(self):
        cost = 0
        node = self
        while not node.parent is None:
            if node.col == node.parent.col or node.row == node.parent.row:
                cost += 10
            else:
                cost += 14
            node = node.parent
        return cost

    def f_cost(self):
        return self.g_cost() + self.h_cost

    def dist(self, node):
        diffs = [abs(self.row - node.row), abs(self.col - node.col)]
        return abs(diffs[0] - diffs[1]) * 10 + min(diffs) * 14

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    def __ne__(self, other):
        return not self.__eq__(other)
    def __str__(self):
        return "(" + str(self.row) + ", " + str(self.col) + ")"
