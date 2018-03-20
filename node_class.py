from vector2_class import Vector2
import math
class Node(object):
    def __init__(self, pos, _guid):
        self.guid = _guid
        self.position = pos
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None
        self.can_traverse = True

    def calc_g_score(self, node):
        '''Calculates the g_score of the nodes in the graph and does tentative_g'''
        if self.position.x_pos == node.position.x_pos and self.position.y_pos == node.position.y_pos:
            return
        if self.parent is None:
            if self.position.x_pos == node.position.x_pos or self.position.y_pos == node.position.y_pos:
                self.g_score = node.g_score + 10
            else:
                self.g_score = node.g_score + 14
            self.parent = node
        if node.parent is not None:
            tentative = self.g_score
            if self.position.x_pos == node.position.x_pos or self.position.y_pos == node.position.y_pos:
                tentative = node.g_score + 10
            else:
                tentative = node.g_score + 14
            if tentative < self.g_score:
                self.g_score = tentative
                self.parent = node
                return

    def calc_h_score(self, node):
        self.h_score = (abs(self.position.x_pos - node.position.x_pos) + abs(self.position.y_pos - node.position.y_pos)) * 10

    def calc_f_score(self):
        self.f_score = self.g_score + self.h_score

    def set_parent(self, node):
        '''Checks the nodes parents and can trace node to start'''
        self.parent = node
