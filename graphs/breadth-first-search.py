from collections import deque

'''
Runtime (Adjacency List): O(|V|+|E|)
Space (Adjacency List): O(|V|+|E|)

Returns a traversal of the graph where all neighbour nodes are visited first before children nodes
The algorithm may not visit all verticies (if the graph is disconnected at some point between nodes)

Other Notes:
- Can be used to find shortest path between two nodes
- Used for web crawlers that index pages 
- Cycle detection in undirected graphs (determining if a cycle exists in the graph)
- Path finding, determining if a path exists between two nodes
'''
def bfs(g, node_to_search_from):

    if not g[node_to_search_from]:
        return

    queue = deque(node_to_search_from)
    visited = []

    while queue:
        curr_node = queue.popleft()
        
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
