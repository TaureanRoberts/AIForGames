from vector2_class import Vector2
class Node(object):
    def __init__(self, pos):
        self.position = pos

class Graph(object):
    def __init__(self, nodes):
        self.nodes = []
        self.dimension = nodes

    def make_nodes(self):
        '''Make a search space for the nodes'''
        for i in range(0, self.dimension):
            _nodes = Node(i)
            self.nodes.append(_nodes)

g = Graph([4])
new_g = g.make_nodes
