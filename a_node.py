from vector2_class import Vector2
class Node(object):
    def __init__(self, pos, traverseable):
        self.position = pos
        self.parent = None
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.is_traversable = traverseable

    def calculate_g_score(self, nodes):
        self.position = nodes

    def node_parent(self, parents):
        self.parent = parents

class Graph(object):
    def __init__(self, dimension):
        self.nodes = []
        self.dimension = dimension

    def make_nodes(self):
        for i in range(0, self.dimension.x_pos):
            for j in range(0, self.dimension.y_pos):
                self.nodes.append(Node(Vector2(i, j), True))

    def find_neighbors(self):
        current