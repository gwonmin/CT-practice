from collections import deque
#bfs

n, m = map(int,input().split())

miro = []

for _ in range(n):
    miro.append(list(input()))

miro[0][0] = 1
# print(*miro,sep='\n')

# 동서남북 방향벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#시작 좌표
dq = deque([[0,0]])

while dq:
    x, y = dq[0][0], dq[0][1]
    dq.popleft()
    #동서남북으로 보내기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if miro[nx][ny] == "1":
                dq.append([nx,ny])
                miro[nx][ny] = miro[x][y] + 1

# print(*miro,sep='\n')
print(miro[n-1][m-1])