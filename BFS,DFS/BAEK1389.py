import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

def bfs(start,end):
    visited = set()
    visit = deque()
    visit.append((start,0))

    while visit:
        v = visit.popleft()
        if v[0] == end:
            return v

        for node in graph[v[0]]:
            if node not in visited:
                visited.add(node)
                visit.append((node,v[1]+1))

kb = 1e9
idx = 0
for i in range(1,n+1):
    temp = 0
    for j in range(1,n+1):
        temp += bfs(i,j)[1]
    if kb > temp:
        kb = temp
        idx = i
print(idx)



