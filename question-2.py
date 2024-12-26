from typing import Dict
import heapq
def uninformed_path_finder(roads:Dict,start_node, end_node,strategy:str):
    '''
    Parameters:
        - cities: List of city names.
        - roads: Dictionary with city connections as {city:
        [(connected_city, distance)]}.
        - start_city: The city to start the journey.
        - goal_city: The destination city (for specific tasks).
        - strategy: The uninformed search strategy to use ('bfs' or
        'dfs').
    Returns:
        - path: List of cities representing the path from start_city to
        goal_city.
        - cost: Total cost (number of steps or distance) of the path.
    '''
    if not(start_node in roads and end_node in roads):
        return []
    stack = [(start_node,[start_node],0)]
    while stack:
        if strategy == 'dfs':
            curr_node,path,cost = stack.pop()
        else:
            curr_node,path,cost = stack.pop(0)
        if curr_node == end_node:
            return path,cost
        for i in roads[curr_node]:
            if i[0] not in path:
                stack.append((i[0],path+[i[0]], cost + i[1]))
    return ([],-1)
def weighted_path_finder(roads, curr_node,end_node):
    '''
        Parameters:
            - roads: a dictionary that can be used as a graph
            - curr_node: the start node that can be used as an initial node
            - end_node: the destination node that the agent wants to go to.
        return:
            - A list containing the path that is traversed.
            - A cost that it takes to traverse the route.
    '''
    priority_queue = []
    start_node = curr_node
    shortest_table = {node: float('inf') for node in roads}
    parent_tracker = {node: '' for node in roads}
    heapq.heappush(priority_queue, (0,curr_node))
    cost = 0
    shortest_table[curr_node] = 0
    while priority_queue:
        path, curr_node = heapq.heappop(priority_queue)
        if curr_node == end_node:
            break
        if shortest_table[curr_node] >= path:
             for neighbor, weight in roads[curr_node]:
                distance = path + weight
                if distance < shortest_table[neighbor]:
                    shortest_table[neighbor] = distance
                    parent_tracker[neighbor] = curr_node
                    heapq.heappush(priority_queue, (distance, neighbor))
    if curr_node == end_node:
        return reconstruct_path(parent_tracker,shortest_table,start_node,end_node)
    else:
        return [],0

def reconstruct_path(dependency_graph,shortest_table,start_node,end_node):
    path = []
    cost = 0
    while start_node != end_node:
        path.insert(0, end_node)
        cost+=shortest_table[end_node]
        end_node = dependency_graph[end_node]
    path.insert(0, start_node)
    return path,cost

roads2 = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
    }

print(uninformed_path_finder(roads2,'Arad','Sibiu','dfs'))
print(uninformed_path_finder(roads2,'Arad', 'Sibiu','bfs'))
print(weighted_path_finder(roads2, 'Arad', 'Sibiu'))