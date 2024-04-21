from collections import deque

# Defining queue
q = deque(maxlen=2)
# Enqueue to queue
q.append(1)
q.append(2)
q.append(3)
# deque pop one element from front if inserting after max length
print(q)
# Dequeue from queue
q.popleft()
q.popleft()
print(q)
# Clear the queue
q.append(2)
q.append(3)
q.clear()
print(q)
