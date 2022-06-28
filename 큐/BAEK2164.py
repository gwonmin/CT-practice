import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
if N == 1:
    print(1)
else:
    for i in range(1,N+1):
        queue.append(i)

    while True:
        queue.popleft()# drop
        if len(queue) == 1:
            break
        card = queue.popleft() 
        queue.append(card)
    print(queue[0])