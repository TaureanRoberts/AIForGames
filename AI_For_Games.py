import math
class Vector2(object):
    def __init__(self, lhs, rhs):
        self.x_pos = lhs
        self.y_pos = rhs
    def __add__(self, other):
        new_vect2 = Vector2(self.x_pos + other.x_pos, self.y_pos + other.y_pos)
        return new_vect2
    def __sub__(self, other):
        new_vect2 = Vector2(self.x_pos - other.x_pos, self.y_pos - self.y_pos)
        return new_vect2
    def __mul__(self, other):
        new_vect2 = Vector2(self.x_pos * other, self.y_pos *other)
        return new_vect2
    def magn(self, other):
        new_vect2 = Vector2(self.x_pos + other.x)
    def norm(self, other):
    def dot(self, other):