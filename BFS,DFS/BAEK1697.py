from collections import deque
import sys

input = sys.stdin.readline
n,k = map(int,input().split())

def bfs(start,end):
    visited = set()
    visited.add(start)
    visit = deque()
    visit.append([start,0])

    while visit:
        pos,time = visit.popleft()

        for i in range(3):
            if i == 0 and pos*2 not in visited and pos*2 <= end+pos:
                if pos*2 == end:
                    return time+1
                visit.append([pos*2,time+1])
                visited.add(pos*2)
            if i == 1 and pos+1 not in visited and pos+1 <= end:
                if pos+1 == end:
                    return time+1
                visit.append([pos+1,time+1])
                visited.add(pos+1)
            if i == 2 and pos-1 not in visited and pos-1 >= 0:
                if pos-1 == end:
                    return time+1
                visit.append([pos-1,time+1])
                visited.add(pos-1)

if n == k:
    print(0)
else:
    print(bfs(n,k))
