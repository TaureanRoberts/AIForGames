from vector2_class import Vector2
class Node(object):
    def __init__(self, pos):
        self.position = pos

class Graph(object):
    def __init__(self, dims):
        self.nodes = []
        self.dimension = dims

    def make_nodes(self):
        '''Make a search space for the nodes'''
        for i in range(0, self.dimension.x_pos):
            for j in range(0, self.dimension.y_pos):
                _node = Node(Vector2(i, j))
                self.nodes.append(_node)

g = Graph(Vector2(4, 4))
new_g = g.make_nodes()
a = 0
