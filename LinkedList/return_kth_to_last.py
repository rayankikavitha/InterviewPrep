from LinkedList import LinkedList

nums = [1,2,5,6,9,7,3,8]
l = LinkedList()
for i in range(len(nums)):
    l.add(nums[i])

l.printlist()

# assuming length of linked list is not known
def return_kth_to_last(ll, k):
    head = ll.head
    curr = head
    # set the runner k positions away from curr
    # if the runner is at last position, curr will be at the kth last
    while curr is not None and k > 0:
        curr = curr.next
        k    = k - 1
    runner = curr

    curr = head
    while runner is not None:
        runner = runner.next
        curr = curr.next
    return curr.val

print "\n"
print return_kth_to_last(l,5)

