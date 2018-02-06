from vector2_class import Vector2
class Graph(object):
    def __init__(self, node, xpos, ypos):
        self.nodes = node
        self.x_position = xpos
        self.y_position = ypos
    def graph_demensions(self, pos):
        self.x_position = pos