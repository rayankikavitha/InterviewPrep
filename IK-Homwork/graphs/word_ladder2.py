from pythonds.graphs import Graph

def buildGraph(wordlist):
    d = {}
    g = Graph()
    # create buckets of words that differ by one letter
    for line in wordlist:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

print buildGraph(["cat","hat","bad","had"]).vertices
