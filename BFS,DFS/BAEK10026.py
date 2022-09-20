import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [input().strip() for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

def bfs(start,color):
    if visited[start[0]][start[1]] or graph[start[0]][start[1]] != color:
        return 0

    visit = deque()
    visit.append(start)

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while visit:
        v = visit.popleft()

        for i in range(4):
            nx = dx[i] + v[0]
            ny = dy[i] + v[1]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color:
                if visited[nx][ny]:
                    continue

                visited[nx][ny] = 1
                visit.append((nx,ny))
    return 1

r = 0
rg = 0

for i in range(n):
    for j in range(n):
        r += bfs((i, j), 'R')
        r += bfs((i, j), 'G')
        r += bfs((i, j), 'B')

graph = [g.replace('G', 'R') for g in graph]
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        rg += bfs((i, j), 'R')
        rg += bfs((i, j), 'B')

print(r)
print(rg)