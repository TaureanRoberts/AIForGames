from vector2_class import Vector2
class Node(object):
    def __init__(self, pos, _guid):
        self.guid = _guid
        self.position = pos
        self.g_score = 0
        self.parent = None

    def calc_g_score(self, node):
        if self.position.x_pos == node.position.x_pos or self.position.y_pos == node.position.y_pos:
            self.g_score = node.g_score + 10
        else:
            self.g_score = node.g_score + 14

    def is_parented(self, node):
        '''Checks the nodes parents and can trace node to start'''
        self.parent = node
        return self.parent
