from node_class import Node
from vector2_class import Vector2
from graph_class import Graph

def algorithm(start_node, goal_node, searchspace):
    open_list = []
    closed_list = []
    current_node = start_node
    # 1. Add the starting square (or node) to the open list
    open_list.append(current_node)
    # 2. Loop as long as the open list is not empty
    while open_list:
        # 2.1 Look for the lowest fscore in the open list
        open_list.sort(key=lambda node: node.f_score)
        # 2.2 Add the current node to the closed list
        # Extra: if the closed node is in the closed list then break
        # 2.3 Find the neighbors of the current node and put them in the open list
        # 2.4 Loop through all the neighbors of the current node
            # 2.4.1 If not traversable or in the closed list
                # Ignore it
            # 2.4.2 If not in the open list
                # add to the open list and calc h, g, f scores
            # 2.4.3 If it is in the open list
                # check if better path
