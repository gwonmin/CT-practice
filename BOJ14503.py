from collections import deque
N, M = map(int, input().split())

x, y, d = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

#서,북,동,남
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = deque()
visited.append([x,y])
count = 0

def robot(visited,d):
    print(*graph, sep='\n')
    global count
    while visited:
        x, y = visited.popleft()
        d = d
        count += 1
        temp = 0
        for i in range(4):
            if d == 0:
                d = 3
            else:
                d -= 1
            if x+dx[d] < M and x+dx[d] >= 0 and y+dy[d] < N and y+dy[d] >= 0:
                print(x+dx[d],y+dy[d])
                if graph[x+dx[d]][y+dy[d]] == 0:
                    visited.append([x+dx[d],y+dy[d]])
                    break
                else:
                    temp += 1
            else:
                continue
        if x - dx[d] < M and x - dx[d] >= 0 and y - dy[d] < N and y - dy[d] >= 0:
            if temp == 4 and graph[x-dx[d]][y-dy[d]] == 1:
                break
            else:
                visited.append([x-dx[d],y-dy[d]])
        else:
            continue

robot(visited,d)
print(count)

# 1.현재 위치를 청소한다.
# 2.현재 위치에서 다음을 반복하면서 인접한 칸을 탐색한다.
    # a.현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면,
    # 왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다.
    # 그렇지 않을 경우, 왼쪽 방향으로 회전한다.
    # 이때, 왼쪽은 현재 바라보는 방향을 기준으로 한다.

    # b.1번으로 돌아가거나 후진하지 않고
    # 2a번 단계가 연속으로 네 번 실행되었을 경우, 바로 뒤쪽이 벽이라면 작동을 멈춘다.

    # 그렇지 않다면 한 칸 후진한다.

# d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽