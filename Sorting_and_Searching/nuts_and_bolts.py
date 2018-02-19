import heapq


def mergearrays(iarray):
    h = []  # heap
    result = []
    # initialize heap with first element and index from each list as a tuple
    for i, v in enumerate(iarray):
        heapq.heappush(h, (v[0], 0, i))  # push item,item index and array index

    while h:
        curr_min_tuple = heapq.heappop(h)
        item, item_index, array_index = curr_min_tuple
        result.append(item)
        if item_index < len(iarray[array_index]) - 1:
            heapq.heappush(h, (iarray[array_index][item_index + 1], item_index + 1, array_index))

    return result
