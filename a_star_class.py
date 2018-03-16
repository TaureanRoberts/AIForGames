from node_class import Node
from vector2_class import Vector2
from graph_class import Graph
import math

def algorithm(start_node, goal_node, graph):
    open_list = []
    closed_list = []
    current_node = start_node
    # 1. Add the starting square (or node) to the open list
    open_list.append(current_node)
    # 2. Loop as long as the open list is not empty
    while open_list:
        # 2.1 Look for the lowest fscore in the open list
        open_list.sort(key=lambda node: node.f_score)
        current_node = open_list[0]
        open_list.remove(current_node)
        # 2.2 Add the current node to the closed list
        closed_list.append(current_node)
        # Extra: if the closed node is in the closed list then break
        if closed_list.__contains__(goal_node):
            current = goal_node
            path = [] #you need to return path at some point
            while current is not None:
                path.append(current) #appends current to the path
                current = current.parent #current gets assigned the
            return path
        # 2.3 Find the neighbors of the current node and put them in the open list
        nays = graph.get_neighbors(current_node) #Finds the neighbors of the current node
        # 2.4 Loop through all the neighbors of the current Node
        for node in nays:
            # 2.4.1 If not traversable or in the closed list
            if closed_list.__contains__(node) or node.can_traverse == False:
                # Ignore it
                continue
            # 2.4.2 If not in the open list
            if node not in open_list:
                # add to the open list and calc h, g, f scores
                open_list.append(node)
            node.calc_g_score(current_node)
            node.calc_h_score(goal_node)
            node.calc_f_score()
            # 2.4.3 If it is in the open list

def main():
    grid = Graph(Vector2(7, 7))
    grid.make_nodes()    
    grid.nodes[23].can_traverse = False
    grid.nodes[24].can_traverse = False
    grid.nodes[25].can_traverse = False
    s = grid.nodes[10]
    g = grid.nodes[38]
    p = algorithm(s, g, grid)
    a = 0

main()

