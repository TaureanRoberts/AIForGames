import math
class Vector2(object):
    def __init__(self, lhs, rhs):
        self.x_pos = lhs
        self.y_pos = rhs

    #Prototype: def __add__(self, other)
    #Descripton: overloads the addidion opperator
    #Arguements: take an arguement of other
    #PreCondition: the node position and adds it to other
    #PostCondition:  Returns sum of the two
    #Protection Level: Public
    def __add__(self, other):
        '''Overloads the addition operator'''
        new_vect2 = Vector2(self.x_pos + other.x_pos, self.y_pos + other.y_pos)
        return new_vect2

    #Prototype: def __sub__(self, other)
    #Descripton: Overloads the subtraction operators
    #Arguements: takes in a arguement 
    #PreCondition: takes the position and subtracts it to a node
    #PostCondition: Returns the new node into 
    #Protection Level: Public
    def __sub__(self, other):
        '''Overloads the subtraction funtions'''
        new_vect2 = Vector2(self.x_pos - other.x_pos, self.y_pos - other.y_pos)
        return new_vect2

    #Prototype: def __mul__(self, other)
    #Descripton: scales the points of the vectors
    #Arguements: Takes an arguement of other
    #PreCondition: takes the current position and scales the values of the current node 
    #PostCondition: returns a scaled version of the current node
    #Protection Level: Public
    def __mul__(self, other):
        '''Scales the vectors'''
        new_vect2 = Vector2(self.x_pos * other, self.y_pos *other)
        return new_vect2

    #Prototype: def dot(self, other)
    #Descripton: Overloads the dot operator
    #Arguements: Takes in an arguement of other
    #PreCondition: takes in the current 
    #PostCondition: returns the combined total
    #Protection Level: Public
    def dot(self, other):
        '''Dot operator overloader'''
        spot = self.x_pos * other.x_pos + self.y_pos * other.y_pos
        return spot

    #Prototype: def magnitude(self)
    #Descripton: gets the
    #Arguements:
    #PreCondition:
    #PostCondition:
    #Protection Level:
    def magnitude(self):
        '''Gets the magnitude of the vector'''
        magn = math.sqrt(self.x_pos * self.x_pos + self.y_pos * self.y_pos)
        return magn

    #Prototype:
    #Descripton:
    #Arguements:
    #PreCondition:
    #PostCondition:
    #Protection Level:
    def normalize(self):
        '''Normalizes the magnitude of the vector'''
        mag = self.magnitude()
        norm = Vector2(self.x_pos / mag, self.y_pos / mag)
        return norm

    #Prototype:
    #Descripton:
    #Arguements:
    #PreCondition:
    #PostCondition:
    #Protection Level:
    def __eq__(self, other):
        '''Overloads the == operator'''
        return (self.x_pos == other.x_pos and self.y_pos == other.y_pos)
        