from vector2_class import Vector2
class Node(object):
    def __init__(self, pos):
        self.guid = pos

class Graph(object):
    def __init__(self, dims):
        self.nodes = []
        self.dimension = dims

    def make_nodes(self):
        '''Make a search space for the nodes'''
        for i in range(self.dimension, self.nodes, +1):
            self.nodes.append(Node(i))

new_node = Graph(4)
