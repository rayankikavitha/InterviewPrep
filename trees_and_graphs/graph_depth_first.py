import Queue as Q

class graphNode():
    def __init__(self,value):
        self.val = value
        self.adjlist = []
        self.visited = False


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

a = graphNode('A')
b = graphNode('B')
c = graphNode('C')
d = graphNode('D')
e = graphNode('E')
f = graphNode('F')
g = graphNode('G')

a.adjlist.append(b)
a.adjlist.append(c)
a.adjlist.append(d)
c.adjlist.append(e)
d.adjlist.append(e)
b.adjlist.append(f)
e.adjlist.append(f)
e.adjlist.append(g)
f.adjlist.append(g)


"""
GRAPH LAYOUT 

  / B ----- F -----  G
A - C - E / -----/
  \ D /
"""
def depth_first(graphNode):
    n = graphNode
    q = Q.Queue()
    # add elements in a adj list to a queue
    if len(n.adjlist) > 0:
        for each_node in n.adjlist:
            q.put(each_node)
    else:
        print n.val
        return
    while (q.get()):
        depth_first(q.get())


depth_first(a)


