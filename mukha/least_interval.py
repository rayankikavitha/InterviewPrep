def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    res = 0
    for i in range(1,len(tasks)):
        if tasks[i] == tasks[i - 1]:
            print tasks[i], tasks[i-1]
            res += n
    return res

print leastInterval(["A","A","A","B","B","B"],2)
