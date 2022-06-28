from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int,input().split())
    result = 0
    baechu = []

    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        x,y = map(int,input().split())
        baechu.append([x,y])
        graph[y][x] += 1

    def bfs(x,y):
        global visited
        global graph

        visit = deque()
        visit.append((x,y))

        visited[y][x] += 1

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        while visit:
            x,y = visit.popleft()

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < M and 0 <= ny < N:
                    if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                        visited[ny][nx] += 1
                        visit.append((nx, ny))

    for i in baechu:
        if visited[i[1]][i[0]] == 0:
            bfs(i[0],i[1])
            result += 1

    print(result)