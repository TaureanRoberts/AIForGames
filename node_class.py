from vector2_class import Vector2
class Node(object):
    def __init__(self, pos, _guid):
        self.guid = _guid
        self.position = pos
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None
        self.traversable = True

    def calc_g_score(self, node_):
        if self.position.x_pos == node_.position.x_pos or self.position.y_pos == node_.position.y_pos:
            self.g_score = node_.g_score + 10
        else:
            self.g_score = node_.g_score + 14

    def calc_h_score(self, node):
        self.h_score = ((self.position.x_pos - node.position.x_pos) + (self.position.y_pos - node.position.y_pos)) * 10

    def calc_f_score(self):
        self.f_score = self.calc_g_score + self.calc_h_score

    def set_parent(self, node):
        '''Checks the nodes parents and can trace node to start'''
        self.parent = node
        return self.parent
