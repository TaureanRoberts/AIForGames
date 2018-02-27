from vector2_class import Vector2
class Node(object):
    def __init__(self, pos, _guid):
        self.guid = _guid
        self.position = pos

class Graph(object):
    def __init__(self, dims):
        self.nodes = []
        self.dimension = dims

    def make_nodes(self):
        '''Make a search space for the nodes'''
        guid = 0
        for i in range(0, self.dimension.y_pos):
            for j in range(0, self.dimension.x_pos):
                _node = Node(Vector2(i, j), guid)
                guid = guid + 1
                self.nodes.append(_node)

    def find_neighbors(self):
        '''Finds nodes that neighbor the current node'''
        guid = Graph(Vector2(4, 4))
        top = guid - self.dimension #Top Node
        bot = guid + self.dimension #Bottom Node
        left = guid - 1 #Left Node
        right = guid + 1 #Right Node
        total_positions = ([top, bot, left, right])
        self.nodes.append(total_positions)

g = Graph(Vector2(4, 4))
pop_g = g.find_neighbors()

