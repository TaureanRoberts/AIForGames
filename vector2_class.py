import math
class Vector2(object):
    def __init__(self, lhs, rhs):
        self.x_pos = lhs
        self.y_pos = rhs

    def __add__(self, other):
        '''Overloads the addition operator'''
        new_vect2 = Vector2(self.x_pos + other.x_pos, self.y_pos + other.y_pos)
        return new_vect2

    def __sub__(self, other):
        '''Overloads the subtraction funtions'''
        new_vect2 = Vector2(self.x_pos - other.x_pos, self.y_pos - other.y_pos)
        return new_vect2

    def __mul__(self, other):
        '''Scales the vectors'''
        new_vect2 = Vector2(self.x_pos * other, self.y_pos *other)
        return new_vect2

    def dot(self, other):
        '''Dot operator overloader'''
        spot = self.x_pos * other.x_pos + self.y_pos * other.y_pos
        return spot

    def magnitude(self):
        '''Gets the magnitude of the vector'''
        magn = math.sqrt(self.x_pos * self.x_pos + self.y_pos * self.y_pos)
        return magn

    def normalize(self):
        '''Normalizes the magnitude of the vector'''
        mag = self.magnitude()
        norm = Vector2(self.x_pos / mag, self.y_pos / mag)
        return norm

    def __eq__(self, other):
        return (self.x_pos == other.x_pos and self.y_pos == other.y_pos)
        