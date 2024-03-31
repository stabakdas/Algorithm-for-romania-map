# Define the Romania map as a dictionary of cities and their neighboring cities
romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucharest': 101, 'Craiova': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Vaslui': 142, 'Bucharest': 85, 'Hirsova': 98},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Oradea': 71, 'Arad': 75}
}

# Define the initial and goal states
initial_state = 'Zerind'
goal_state = 'Bucharest'

# Define the search tree constructed algorithm specific to each strategy

# Breadth-First Search
def bfs(initial_state, goal_state, map):
    frontier = [(initial_state, [])]
    explored = set()
    
    while frontier:
        state, path = frontier.pop(0)
        if state == goal_state:
            return path + [state], len(path) + 1
        explored.add(state)
        for neighbor, _ in map[state].items():
            if neighbor not in explored:
                frontier.append((neighbor, path + [state]))
    
    return None, None

# Depth-First Search
def dfs(initial_state, goal_state, map):
    frontier = [(initial_state, [])]
    explored = set()
    
    while frontier:
        state, path = frontier.pop()
        if state == goal_state:
            return path + [state], len(path) + 1
        explored.add(state)
        for neighbor, _ in map[state].items():
            if neighbor not in explored:
                frontier.append((neighbor, path + [state]))
    
    return None, None

import heapq
# Uniform Cost Search
def ucs(initial_state, goal_state, map):
    frontier = [(0, initial_state, [])]  # Priority queue with cost, state, and path
    explored = set()
    
    while frontier:
        cost, state, path = heapq.heappop(frontier)
        if state == goal_state:
            return path + [state], cost
        explored.add(state)
        for neighbor, neighbor_cost in map[state].items():
            if neighbor not in explored:
                heapq.heappush(frontier, (cost + neighbor_cost, neighbor, path + [state]))
    
    return None, None
   
# Perform BFS
bfs_path, bfs_length = bfs(initial_state, goal_state, romania_map)
print("BFS Path:", bfs_path)
print("BFS Length:", bfs_length)

# Perform DFS
dfs_path, dfs_length = dfs(initial_state, goal_state, romania_map)
print("DFS Path:", dfs_path)
print("DFS Length:", dfs_length)

# Perform UCS
ucs_path, ucs_cost = ucs(initial_state, goal_state, romania_map)
print("UCS Path:", ucs_path)
print("UCS Cost:", ucs_cost)
