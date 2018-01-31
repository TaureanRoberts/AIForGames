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
    def magnitude(self):
        '''Gets the magnitude of the vector'''
        magn = math.sqrt(self.x_pos * self.x_pos + self.y_pos * self.y_pos)
        return magn
    def normalize(self):
        '''Normalizes the magnitude of the vector'''
        mag = self.magnitude()
        norm = Vector2(self.x_pos / mag, self.y_pos / mag)
        return norm
    def dot(self, other):
        '''Dot operator overloader'''
        spot = Vector2(self.x_pos * other.x_pos, self.y_pos * other.y_pos)
        return spot
