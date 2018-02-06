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