'''
Runtime (Adjacency List): O(|V|+|E|)
Space (Adjacency List): O(|V|+|E|)

Returns a traversal of the graph where all child nodes are visited first before neighbours nodes

Other Notes:
- Can be used to find if a path exists between two vertices (path finding)
- Is used to determine if a cycle exists in a graph
- Used to solve puzzles that only have one solution (i.e. mazes)
'''

def dfs(g, node_to_start_from):

    if not g[node_to_start_from]:
        return []

    visited = []
    stack = [node_to_start_from]

    while stack:
        curr_node = stack.pop()

        if curr_node not in visited:
            visited.append(curr_node)
            children = graph[curr_node]

            for child in children:
                stack.append(child)

    return visited


graph = {'A': ['B', 'C', 'E'],
         'B': ['D', 'E'],
         'C': ['A'],
         'D': ['E'],
         'E': ['C']
         }
    
print (dfs(graph, 'A'))