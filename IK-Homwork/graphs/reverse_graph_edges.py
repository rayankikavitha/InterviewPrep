
"""
Build a new graph with reversed edges
for n = 3, nodes[1,2,3]
edges = [ (1->2), (2->3)
#output = [(2->1),(3->2),...]

Don't modify input graph, return new graph
"""

class Node:
    def __init__(self):
        self.neighbors=[]
        self.val = None


def build_other_graph(node):
    newgraph ={}
    #stack to store neighboring nodes
    s=[]
    for each in node.neighbors:
        s.append((each,node))
    while s:
        curneigh = s.pop()
        newgraph[curneigh[0]] = curneigh[1]
        for each in curneigh[0].neighbors:
            if each not in s:
                s.append( (each,curneigh[0]))
    return newgraph.keys[0]

def build_other_graph(node):

    while node.neighbors:
        newn = Node()
        temp = node
        newn  = node.neighbors[0]
        newn.neighbors.append(temp)
        node = node.neighbors[0]
    return newn

