from collections import deque
N,M,K = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

king = []

for x in range(N):
    for y in range(M):
        if graph[x][y] == 4:
            start = (x,y)
        elif graph[x][y] == 3:
            king.append((x,y))

visited = [[0]*M for _ in range(N)]

#pos is tuple
def dfs(pos):
    visit = deque([pos])
    x, y = visit[0]
    visited[x][y] = 1

    result = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while visit:
        x, y = visit.popleft()

        if graph[x][y] == 2:
            return result

        elif len(visit) == 0:
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < N and 0 <= ny < M:
                    route = (nx,ny)
                    if visited[nx][ny] != 1 and graph[nx][ny] != 1:
                        for k in king:
                            if (abs(nx - k[0]) + abs(ny - k[1])) > K:
                                visit.append(route)
                                visited[nx][ny] = 1
                                print(*visited,sep='\n')
            result += 1
        print(result)

print(dfs(start))
print(*graph,sep='\n')

