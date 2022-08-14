import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

start_lst = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 1:
            start_lst.append([i,j])
        if graph[i][j] == -1:
            visited[i][j] = 1

def bfs(start_lst):
    global visited
    visit = deque()

    for start in start_lst:
        visit.append(start)
        visited[start[0]][start[1]] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while visit:
        pos = visit.popleft()

        for i in range(4):
            nx = dx[i] + pos[0]
            ny = dy[i] + pos[1]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] != -1:
                    visit.append([nx,ny])
                    visited[nx][ny] = visited[pos[0]][pos[1]] + 1

    return visited

min_num = 1e9
max_num = -1e9

result_lst = bfs(start_lst)
for r in result_lst:
    for a in r:
        min_num = min(min_num,a)
        max_num = max(max_num,a)

if min_num == 0:
    print(-1)
elif min_num == max_num:
    print(0)
else:
    print(max_num-1)


