from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
dq = deque()

for _ in range(n):
    s = input().strip()
    if s[-1].isnumeric():
        order ,num = s.split()
        num = int(num)
        dq.append(num)
    else:
        if s == 'pop':
            if len(dq) == 0:
                print(-1)
            else:
                print(dq.popleft())
        elif s == 'size':
            print(len(dq))
        elif s == 'empty':
            if len(dq) == 0:
                print(1)
            else:
                print(0)
        elif s == 'front':
            if len(dq) == 0:
                print(-1)
            else:
                print(dq[0])
        else:
            if len(dq) == 0:
                print(-1)
            else:
                print(dq[-1])