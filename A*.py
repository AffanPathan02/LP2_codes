def A_star(start_state, goal_state, heuristic_function, successors_function):
    open_set = [start_state]
    came_from = {start_state: None}
    g_score = {start_state: 0}
    f_score = {start_state: heuristic_function(start_state, goal_state)}

    while open_set:
        current_state = min(open_set, key=lambda state: f_score[state])
        open_set.remove(current_state)
        
        if current_state == goal_state:
            path = [current_state]
            while path[-1] in came_from:
                path.append(came_from[path[-1]])
            path.reverse()
            return path

        for successor in successors_function(current_state):
            new_g_score = g_score[current_state] + successor.cost
            if successor.state not in g_score or new_g_score < g_score[successor.state]:
                g_score[successor.state] = new_g_score
                f_score[successor.state] = new_g_score + heuristic_function(successor.state, goal_state)
                came_from[successor.state] = current_state
                if successor.state not in open_set:
                    open_set.append(successor.state)

    return None
