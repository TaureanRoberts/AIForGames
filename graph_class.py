from node_class import Node
from vector2_class import Vector2
class Graph(object):
    def __init__(self, dims):
        self.nodes = []
        self.dimension = dims

    def make_nodes(self):
        '''Make a search space for the nodes'''
        id = 0
        for i in range(0, self.dimension.x_pos):
            for j in range(0, self.dimension.y_pos):
                _node = Node(Vector2(i, j), id)
                id = id + 1
                self.nodes.append(_node)

    def find_neighbors(self, guid):
        '''Finds the neighbors by getting their guid to give position'''
        top = guid - self.dimension.x_pos  # Top Node
        bot = guid + self.dimension.x_pos  # Bottom Node
        left = guid - 1  # Left Node
        right = guid + 1  # Right Node
        topl = top + 1  # Top Left node
        topr = top - 1  # Top Right node
        botl = bot + 1  # Bottom Left node
        botr = bot - 1  # Bottom Right node
        total_pos = [top, bot, left, right, topl, topr, botl, botr]
        neighbors = []
        for node in self.nodes:
            if total_pos.__contains__(node.guid):
                neighbors.append(node)
        return neighbors

    def get_neighbors(self, graph):
        '''Gets the position of neighbors by x and y positions'''
        positions = []
        positions.append(graph.position + Vector2(1, 0)) #right
        positions.append(graph.position + Vector2(-1, 0)) #left
        positions.append(graph.position + Vector2(0, 1)) #top
        positions.append(graph.position + Vector2(0, -1)) #bot
        positions.append(graph.position + Vector2(1, 1)) #top_right
        positions.append(graph.position + Vector2(-1, 1)) #top_left
        positions.append(graph.position + Vector2(1, -1)) #bot_right
        positions.append(graph.position + Vector2(-1, -1)) #bot_left
        neighbors = []
        for pos in positions:
            for graph in self.nodes:
                if graph.position == pos:
                    neighbors.append(graph)
        return neighbors
