from collections import deque

#bfs
N = int(input())
graph = [[int(s) for s in input()] for _ in range(N)]
visited = [[0]*N for _ in range(N)]

danji = 0
house_lst = []

def bfs(x,y):
    global visited
    house = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    visit = deque([(x,y)])
    visited[x][y] += 1

    while visit:
        x, y = visit.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visit.append((nx,ny))
                    visited[nx][ny] += 1
                    house += 1
    return house

for x in range(N):
    for y in range(N):
        if graph[x][y] == 1 and visited[x][y] == 0:
            house_lst.append(bfs(x,y))
            danji += 1

print(danji)
house_lst.sort()
for i in house_lst:
    print(i)