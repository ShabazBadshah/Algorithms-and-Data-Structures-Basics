from collections import deque

def bfs(g, node_to_search_from):

    if not g[node_to_search_from]:
        return

    queue = deque(node_to_search_from)
    visited = []

    while queue:
        curr_node = queue.pop()
        
        if curr_node not in visited:
            visited.append(curr_node)
            children = graph[curr_node]

            for child in children:
                queue.append(child)
                
    return visited
        

graph = {'A': ['B', 'C', 'E'],
         'B': ['D', 'E'],
         'C': ['A'],
         'D': ['E'],
         'E': ['C']
         }

print bfs(graph, 'A')
