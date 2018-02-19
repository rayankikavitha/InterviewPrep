"""
given a list of emp_id, manager_id pair and manager_id -  print manager hierarchy, starting at that manager
input = [(1,3),(2,3),(3,4)], manager_id = 4
return = {4:[3],3:[1,2]}
"""
import collections
# create hashmap and do breadth-first search
def create_org(input):
    """
    takes input and returns org structure hierarcy as adjecency list
    :param input:
    :return:
    """
    org = collections.defaultdict(list)
    for e,m in input:
        org[m] += [e]
    return org

def bfs(input,mid):
    org = create_org(input)
    #print org
    q = []
    q = [mid]
    result = collections.defaultdict(list)
    while q:
        currm = q.pop()
        if org[currm]:
            result[currm] += org[currm]
            q += org[currm]
    return result

print bfs([(1,3),(2,3),(3,4),(5,4),(4,6),(10,5)],)



# This one uses recursion

def org_struct(input,id):
    hierarchy= collections.defaultdict(list)
    result = collections.defaultdict(list)
    print hierarchy
    # create hierarchy
    for e,m in input:
        hierarchy[m].append(e)
    print hierarchy
    helper(hierarchy,[id],result)
    return result

def helper(org, mid, result):
    if len(mid) > 1:
        if len(org[mid[0]]) > 0:
            result[mid[0]] += org[mid[0]]
        helper(org,mid[1:],result)
    elif len(mid) == 1:
        if len(org[mid[0]]) > 0:
            result[mid[0]] += org[mid[0]]
            helper(org,org[mid[0]],result)
    else:
        return



#print org_struct([(1,3),(2,3),(3,4),(5,4),(4,6),(10,5)],4)