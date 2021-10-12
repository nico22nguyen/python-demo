from Node_obj import Node
#node constants
WIDTH = 20
HEIGHT = 20
MARGIN = 5

#window constants
WINDOW_SIZE = [505, 505]
START_BUTTON_OFFSET = 6
NUM_ROWS = WINDOW_SIZE[0] // (HEIGHT + MARGIN) - START_BUTTON_OFFSET
NUM_COLUMNS = WINDOW_SIZE[1] // (WIDTH + MARGIN)

class Grid:
    #start - tuple in the form (row, col) denoting start position
    #target - tuple in the form (row, col) denoting intended target
    #obs - list of tuples in the form [(row, col), ...]
    def __init__(self, start, target):
        self.obstacles = []
        self.open = []
        self.closed = []

        #setup target node pointer
        if target is not None:
            self.target = Node(target[0], target[1], 0, None)
        else:
            self.target = None

        #setup start node pointer
        if start is not None:
            self.start = Node(start[0], start[1], self.dist_to_target(start), None)
            self.open.append(self.start)
        else:
            self.start = None


    #creates node for each neighbor and returns list of all neighbors
    def get_neighbors(self, node):
        neighbors = []
        if node.row > 0:
            #North
            if (node.row - 1, node.col) not in self.obstacles:
                neighbors.append(Node(node.row - 1, node.col, 
                                    self.dist_to_target((node.row - 1, node.col)),
                                    node))
            #Northeast
            if node.col < NUM_COLUMNS - 1 and (node.row - 1, node.col + 1) not in self.obstacles:
                neighbors.append(Node(node.row - 1, node.col + 1,
                                    self.dist_to_target((node.row - 1, node.col + 1)),
                                    node))
            #Northwest
            if node.col > 0 and (node.row - 1, node.col - 1) not in self.obstacles:
                neighbors.append(Node(node.row - 1, node.col - 1,
                                    self.dist_to_target((node.row - 1, node.col - 1)),
                                    node))
        if node.row < NUM_ROWS - 1:
            #South
            if (node.row + 1, node.col) not in self.obstacles:
                neighbors.append(Node(node.row + 1, node.col,
                                    self.dist_to_target((node.row + 1, node.col)),
                                    node))
            #Southeast
            if node.col < NUM_COLUMNS - 1 and (node.row + 1, node.col + 1) not in self.obstacles:
                neighbors.append(Node(node.row + 1, node.col + 1,
                                    self.dist_to_target((node.row + 1, node.col + 1)),
                                    node))
            #Southwest
            if node.col > 0 and (node.row + 1, node.col - 1) not in self.obstacles:
                neighbors.append(Node(node.row + 1, node.col - 1,
                                    self.dist_to_target((node.row + 1, node.col - 1)),
                                    node))
        #East
        if node.col < NUM_COLUMNS - 1 and (node.row, node.col + 1) not in self.obstacles:
            neighbors.append(Node(node.row, node.col + 1,
                                    self.dist_to_target((node.row, node.col + 1)),
                                    node))
        #West
        if node.col > 0 and (node.row, node.col - 1) not in self.obstacles:
            neighbors.append(Node(node.row, node.col - 1,
                                    self.dist_to_target((node.row, node.col - 1)),
                                    node))

        return neighbors

    #gives distance to target from point (row, col)
    def dist_to_target(self, point):
        diffs = [abs(self.target.row - point[0]), abs(self.target.col - point[1])]
        return abs(diffs[0] - diffs[1]) * 10 + min(diffs) * 14

    def single_a_star_iter(self):
        #choose open node with lowest fcost
        current = self.open[0]
        for node in self.open:
            if node.f_cost() < current.f_cost() or node.f_cost() == current.f_cost() and node.h_cost < current.h_cost:
                current = node

        #put current in closed
        self.open.remove(current)
        if not current in self.closed:
            self.closed.append(current)

        #found the path
        if current == self.target:
            self.target = current
            return False

        for neighbor in self.get_neighbors(current):
            #invalid neighbor
            if neighbor in self.closed:
                continue

            #replace placeholder nodes with real nodes
            for node in self.open:
                if node == neighbor:
                    neighbor = node
            if not neighbor in self.open or current.g_cost() + current.dist(neighbor) < neighbor.g_cost():
                neighbor.parent = current
                if not neighbor in self.open:
                    self.open.append(neighbor)
        return True