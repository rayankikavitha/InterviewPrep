
# tell if the tree is a binary search tree


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


def graph_dfs(node):
	if node is None:
		return 
	s=[node]
	visited = set()
	while s:
		curnode = s.pop()
		if curnode.visited == False and curnode.val not in visited:
			print (curnode.val)
			curnode.visited = True
			s += [ curnode.adjlist ]
			visited.add(curnode.val)




print (graph_dfs(a))








"""
GRAPH LAYOUT 

  / B ----- F -----  G
A - C - E / -----/
  \ D /




input = ['opts','foo','bar','tops','pots','rab','ofo','hat']
output = [ ['opts','tops','pots'],['rab','bar'],['ofo','foo'],['hat']]

def anagramsets(given):
	d = {}
	result =[]
	for word in given:
		key = ''.join(sorted(word))
		if key in d:
			d[key].append(word)
		else:
			d[key]=[word]
	print (d)
	return d.values()

#print (anagramsets(input))
"""

