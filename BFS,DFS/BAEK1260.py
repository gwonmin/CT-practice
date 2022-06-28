#DFS와 BFS
from collections import deque

n, m, v = map(int,input().split())

graph = [[] for _ in range(n+1)]
line = [list(map(int,input().split())) for _ in range(m)]

for i in range(1,n+1):
    for lst in line:
        if i == lst[0]:
            graph[i].append(lst[1])
        elif i == lst[1]:
            graph[i].append(lst[0])
        else:
            continue

graph = [sorted(node) for node in graph]
visited = [False]*(n+1)

def dfs(graph,v,visted):
    visted[v] = True
    print(v, end=' ')
    if v == len(graph):
        return

    for i in graph[v]:
        if not visted[i]:
            dfs(graph,i,visted)

def bfs(graph, start ,visited):

    dq = deque([start])
    visited[start] = True

    while dq:
        v = dq.popleft()
        print(v, end=' ')
        if v == len(graph):
            return

        for i in graph[v]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True

dfs(graph, v, visited)
visited = [False] * (n + 1)
print()
bfs(graph, v, visited)
