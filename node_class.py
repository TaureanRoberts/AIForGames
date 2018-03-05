from vector2_class import Vector2
class Node(object):
    def __init__(self, pos, _guid):
        self.guid = _guid
        self.position = pos
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None

    def calc_g_score(self, node):
        if self.position.x_pos == node.position.x_pos or self.position.y_pos == node.position.y_pos:
            self.g_score = node.g_score + 10
        else:
            self.g_score = node.g_score + 14

    def calc_h_score(self, node):
        get_hscore = ((self.position.x_pos - node.position.x_pos) * (self.position.y_pos - node.position.y_pos)) * 10
        return get_hscore

    def calc_f_score(self):
        for i in range(0, self.position.x_pos):
            for j in range(0, self.position.y_pos):
                get_fscore = self.calc_g_score(Vector2(i, j)) + self.calc_h_score(Vector2(i, j))
                return get_fscore

    def node_parent(self, node):
        '''Checks the nodes parents and can trace node to start'''
        self.parent = node
        return self.parent
