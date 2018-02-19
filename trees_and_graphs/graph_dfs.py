graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
"""
Mark the current vertex as being visited.
Explore each adjacent vertex that is not included in the visited set.
"""
def dfs(graph,start):
    """
    :param graph: adjency list
    :param start: starting node
    :return: visted : graph values based on visited order
    """
    visited = set()
    stack  = [start] # add starting node to the stack
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
        stack.extend(graph[vertex] - visited) # extend, extends a list with another list.
    return visited


print dfs(graph,'A')

def bfs(graph,start):
    """
    :param graph: adjency list
    :param start: starting node
    :return: visted : graph values based on visited order
    """
    visited = set()
    queue  = [start] # add starting node to the stack
    while queue:
        vertex = queue.pop(0)
        print queue
        print visited
        if vertex not in visited:
            visited.add(vertex)
        queue.extend(graph[vertex] - visited) # extend, extends a list with another list.
    return visited

print "bfs = "
print bfs(graph,'A')

"""
Using recursion
"""

def dfs1(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    for each_node in graph[start] - visited:
        dfs1(graph,each_node, visited)
    return visited

print dfs1(graph, 'A')


