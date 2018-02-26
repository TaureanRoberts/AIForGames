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
        for i in range(0, self.dimension.x_pos):
            for j in range(0, self.dimension.y_pos):
                _node = Node(Vector2(i, j), +1)
                self.nodes.append(_node)

    def find_neighbors(self):
        '''Finds nodes that neighbor the current node'''
        top = self.nodes - self.dimension.x_pos #Top Node
        bot = self.nodes + self.dimension.x_pos #Bottom Node
        left = self.nodes - 1 #Left Node
        right = self.nodes + 1 #Right Node
        topl = top - 1 #TopLeft Node
        topr = top + 1 #TopRight Node
        botl = bot - 1 #BottomLeft Node
        botr = bot + 1 #BottomRight Node
        total_positions = [top, bot, left, right, topl, topr, botl, botr]
        self.nodes.append(total_positions)

g = Graph(Vector2(4, 4))
new_g = g.make_nodes()
print new_g
