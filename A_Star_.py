from AI_For_Games import Vector2
class Node(object):
    def __init__(self, pos, move):
        self.position = pos
        self.movement = move
    def g_score(self, other):
        move = Vector2(self.movement + self.position, self.movement + self.position)
        return move
    def h_score(self):
        