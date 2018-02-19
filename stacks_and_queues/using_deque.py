from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print queue
print list(queue)

print queue.popleft()
print queue.pop()

print queue


print queue.appendleft(5)

print queue.count(2)
queue.reverse()
print queue

