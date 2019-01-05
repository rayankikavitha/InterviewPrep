l=[[3,5,7,8],[4,5,9],[6,6,6,10],[5,9]]
import heapq
def merge_k_sorted_lists(input):
    h=[]
    res=[]
    # add first element to the heap
    for i,v in enumerate(input):
        heapq.heappush(h, (v[0],0, i))
    while h:
        m = heapq.heappop(h)
        item, item_index, array_index = m
        res.append(item)
        if item_index < len(input[array_index]) -1 :
            heapq.heappush(h, (input[array_index][item_index+1],item_index +1, array_index))
        print h
    return res

#print merge_k_sorted_lists(l)


def  mergearrays(iarray):
    h=[] #heap
    result=[]
    #initialize heap with first element and index from each list as a tuple
    for i,v in enumerate(iarray):
        heapq.heappush(h,(v[0],0,i))  # push item,item index and array index

    while h:
        curr_min_tuple = heapq.heappop(h)
        item,item_index,array_index = curr_min_tuple
        result.append(item)
        if item_index < len(iarray[array_index]) -1 :
            heapq.heappush(h,(iarray[array_index][item_index+1], item_index+1, array_index))
        print h
    return result

print mergearrays([[0,1],[0,2]])