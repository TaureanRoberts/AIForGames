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
        self.traversable = True

    def calc_g_score(self, node):
        '''Calculates the g_score of the nodes in the graph and does tentative_g'''
        tentative_g = self.g_score #Assigned to gscore for usage of tentative_g
        if self.position.x_pos == node.position.x_pos and self.position.y_pos == node.position.y_pos:
            return
        if self.position.x_pos == node.position.x_pos or self.position.y_pos == node.position.y_pos:
            tentative_g = node.g_score + 10
        else:
            tentative_g = node.g_score + 14
        if node.parent is not None:
            if tentative_g < self.g_score:
                self.g_score = tentative_g
                self.parent = node
                return
        self.g_score = tentative_g
        self.parent = node

    def calc_h_score(self, node):
        self.h_score = (abs(self.position.x_pos - node.position.x_pos) + abs(self.position.y_pos - node.position.y_pos)) * 10

    def calc_f_score(self):
        self.f_score = self.g_score + self.h_score

    def set_parent(self, node):
        '''Checks the nodes parents and can trace node to start'''
        self.parent = node
