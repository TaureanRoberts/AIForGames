from node_class import Node
from vector2_class import Vector2
class Graph(object):
    def __init__(self, dims):
        self.nodes = []
        self.dimension = dims
        self.g_score = 0

    def make_nodes(self):
        '''Make a search space for the nodes'''
        guid = 0
        for i in range(0, self.dimension.y_pos):
            for j in range(0, self.dimension.x_pos):
                _node = Node(Vector2(i, j), guid)
                guid = guid + 1
                self.nodes.append(_node)

    def find_neighbors(self, guid):
        '''Finds nodes that neighbor the current node'''
        top = guid - self.dimension.x_pos  # Top Node
        bot = guid + self.dimension.x_pos  # Bottom Node
        left = guid - 1  # Left Node
        right = guid + 1  # Right Node
        topl = top - 1  # Top Left node
        topr = top + 1  # Top Right node
        botl = bot - 1  # Bottom Left node
        botr = bot + 1  # Bottom Right node
        total_positions = [top, bot, left, right, topl, topr, botl, botr]
        self.nodes.append(total_positions)

g = Graph(Vector2(4, 4))
new_g = g.find_neighbors(5)
print new_g