def findLadders(dict, start, end,):
    dict.append(start)
    dict.append(end)

    result =[] # to store results
    cur = [start]  # like a queue
    visited = set([start])
    found = False
    trace = {word:[] for word in dict}

    while cur and not found:
        for word in cur:
            visited.add(word)

        next = set()
        for word in cur:
            for i in xrange(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    candidate = word[:i] + j + word[i + 1:]
                    if candidate not in visited and candidate in dict:
                        if candidate == end:
                            found = True
                        next.add(candidate)
                        trace[candidate].append(word)
        cur = next
    print result, trace
    if found:
        backtrack(result, trace, [], end)

    return result


def backtrack( result, trace, path, word):
    if not trace[word]:
        result.append([word] + path)
    else:
        for prev in trace[word]:
            backtrack(result, trace, [word] + path, prev)

import collections
import string
def findLadders2(dic, start, end):
    dic.append(end)
    level = {start}
    parents = collections.defaultdict(set)
    while level and end not in parents:
        next_level = collections.defaultdict(set)
        for node in level:
            for char in string.ascii_lowercase:
                for i in range(len(start)):
                    n = node[:i]+char+node[i+1:]
                    if n in dic and n not in parents:
                        next_level[n].add(node)
        level = next_level
        parents.update(next_level)
    res = [[end]]
    while res and res[0][0] != start:
        res = [[p]+r for r in res for p in parents[r[0]]]
    return res


print findLadders(["cat","hat","bad","had"], "bat","had")
print findLadders2(["cat","hat","bad","had"], "bat","had")
