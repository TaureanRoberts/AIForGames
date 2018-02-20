from vector2_class import Vector2
class Node(object):
    def __init__(self, pos, guid):
        self.position = pos
        self.parent = None
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.is_traversable = True
        self.current_guid = guid

    def calculate_g_score(self, nodes):
        #checks the g score of the current nodes neighbors
        if self.position.x_pos == nodes.position.x_pos or self.position.y_pos == nodes.position.y_pos:
            self.g_score = nodes.g_score + 10
        else:
            self.g_score = nodes.g_score + 14

    def node_parent(self, a_parent):
        self.parent = a_parent

class Graph(object):
    def __init__(self, dims, graph):
        '''dimension is the n*n (heightxwidth) of grid ex: Graph(10) will make a 10x10 graph'''
        self.nodes = []
        self.dimension = dims

    def make_nodes(self):
        #Makes the nodes
        for i in range(0, self.dimension.x_pos):
            for j in range(0, self.dimension.y_pos):
                self.nodes.append(Node(Vector2(i, j), True))

def get_neighbors(guid, graph):
    right = guid.current_guid + 1
    left = guid.current_guid - 1
    top = guid.current_guid - graph.dimension
    bot = guid.current_guid + graph.dimension
    total = ([right, left, top, bot])
    return total

def main():
    g = Graph(4)
    n = Node(5)
    nays = get_neighbors(n, g)
    print nays

main()

new_node = Node(Vector2(0, 2), True)
new_vect2 = Node(Vector2(-1, 2), True)
new_node.calculate_g_score(new_vect2)
