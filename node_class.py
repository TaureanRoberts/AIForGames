from vector2_class import Vector2
class Node(object):
    def __init__(self, pos, _guid):
        self.guid = _guid
        self.position = pos
        self.g_score = 0

    def calc_g_score(self, node):
        if self.position.x_pos == node.position.x_pos or self.position.y_pos == node.position.y_pos:
            self.g_score = node.g_score + 10
        else:
            self.g_score = node.g_score + 14
