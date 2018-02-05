from AI_For_Games import Vector2
class Node(object):
    def __init__(self, pos, move):
        self.position = pos
        self.movement = move
    def g_score(self, other):
        move = Node(self.movement + self.position)
        return move
