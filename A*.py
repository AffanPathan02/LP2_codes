def A_star(start_state, goal_state, heuristic, successors):
    # Initialize the open set, the came-from map, the g score map, and the f score map
    open_set = [start_state]
    came_from = {start_state: None}
    g_score = {start_state: 0}
    f_score = {start_state: heuristic(start_state, goal_state)}
    
    while open_set:
        # Find the state with the lowest f score in the open set
        current_state = min(open_set, key=lambda state: f_score[state])
        
        if current_state == goal_state:
            # We have found the goal state, so reconstruct and return the path
            path = [current_state]
            while came_from[current_state] is not None:
                current_state = came_from[current_state]
                path.append(current_state)
            path.reverse()
            return path
        
        open_set.remove(current_state)
        
        # Generate the successors of the current state
        for successor_state, cost in successors(current_state):
            tentative_g_score = g_score[current_state] + cost
            
            if successor_state not in g_score or tentative_g_score < g_score[successor_state]:
                # This is a better path to the successor, so update the came-from, g score, and f score maps
                came_from[successor_state] = current_state
                g_score[successor_state] = tentative_g_score
                f_score[successor_state] = tentative_g_score + heuristic(successor_state, goal_state)
                if successor_state not in open_set:
                    # Add the successor to the open set if it's not already there
                    open_set.append(successor_state)
    
    # If we get here, we were not able to find a path to the goal state
    return None

def heuristic(state, goal_state):
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

def successors(state):
    x, y = state
    successors = []
    if x > 0:
        successors.append(((x-1, y), 1))
    if x < 4:
        successors.append(((x+1, y), 1))
    if y > 0:
        successors.append(((x, y-1), 1))
    if y < 4:
        successors.append(((x, y+1), 1))
    return successors

start_state = (0, 0)
goal_state = (4, 4)
path = A_star(start_state, goal_state, heuristic, successors)
print(path)
