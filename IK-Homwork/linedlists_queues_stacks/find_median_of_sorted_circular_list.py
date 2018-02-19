def find_median(ptr):
    random = ptr
    pv = ptr.val
    counter = 1
    while random.next.val != pv:
        counter += 1
        random = random.next
    # print counter
    # decide the actual starting point:
    start_val = ptr.val
    newptr = ptr
    while newptr.next.val > start_val:
        newptr = newptr.next
    actual_start = newptr.next
    print actual_start.val
    # decide even or odd using counter
    # odd - mid , mid+1 /2
    mid = counter / 2
    print mid

    while mid > 0:
        prev = actual_start
        actual_start = actual_start.next
        mid -= 1
    if counter % 2 != 0:
        return actual_start.val
    else:
        return (prev.val + actual_start.val) / 2