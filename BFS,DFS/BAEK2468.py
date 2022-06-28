from collections import deque

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
max_h = 0
min_h = 100000000000

for g in graph:
    max_h = max(max_h, max(g))
    min_h = min(min_h, min(g))

def safe_zone(rain,graph):
    visited = [[0]*N for _ in range(N)]
    xy_lst = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] <= rain:
                visited[i][j] += 1
            else:
                xy_lst.append((i,j))

    def bfs(x,y):
        visit = deque()
        visit.append((x,y))
        visited[y][x] += 2

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        while visit:
            x,y = visit.popleft()

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < N and 0 <= ny < N:
                    if visited[ny][nx] == 0:
                        visit.append((nx,ny))
                        visited[ny][nx] += 2
    result = 0
    for i in xy_lst:
        if visited[i[0]][i[1]] == 0:
            bfs(i[1],i[0])
            result += 1

    return result

result = 1

for rain in range(max_h):
    case = safe_zone(rain, graph)
    result = max(result,case)

print(result)