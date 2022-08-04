maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
from collections import deque

def solution(maps):
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[0][0] = 1

    m = len(maps[0])-1
    n = len(maps)-1

    def bfs(maps,start):
        visit = deque()
        visit.append(start)

        while visit:
            v = visit.popleft()
            #동서남북
            dx = [1,-1,0,0]
            dy = [0,0,1,-1]

            for i in range(4):
                x = dx[i] + v[1]
                y = dy[i] + v[0]

                if visited[n][m] != 0:
                    return visited[n][m]

                if 0 <= x <= m and 0 <= y <= n:
                    if maps[y][x] == 1 and visited[y][x] == 0:
                        visited[y][x] += (visited[v[0]][v[1]]+1)
                        visit.append([y,x])

        return -1
    return bfs(maps,[0,0])

print(solution(maps))