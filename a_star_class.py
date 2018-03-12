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
        nays = Graph.find_neighbors(current_node.guid) #Finds the neighbors of the current node
        # 2.4 Loop through all the neighbors of the current Node
        for node in nays:
            # 2.4.1 If not traversable or in the closed list
            if closed_list.__contains__(node):
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
            if open_list.__contains__(node): #Use Tentative G
                # check if better path
                tentative_g == current_node + 10 # horizontal and vertical
                tentative_g == current_node + 14 # diagnal
                if tentative_g < gscore:
                    gscore = tentative_g
                    node.set_parent = current_node
