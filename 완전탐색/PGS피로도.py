#1
k=80
dungeons=[[80,20],[50,40],[30,10]]
from itertools import permutations

def solution(k,dungeons):
    answer = 0

    def check(k,permu):
        max_count = 0
        for p in permu:
            temp = k
            count = 0
            for c in p:
                need = c[0]
                use = c[1]
                if temp >= need:
                    temp -= use
                    count += 1
                else:
                    count = 0
                    break

            max_count = max(max_count, count)
        return max_count

    for i in range(1, len(dungeons) + 1):
        permu = list(permutations(dungeons, i))
        answer = max(answer, check(k, permu))

    return answer

print(solution(k,dungeons))

#2 dfs
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    print(visited)
    dfs(k, 0, dungeons)
    return answer

print(solution(k,dungeons))

#3 bfs

from collections import deque

def solution(k, dungeons):
    visit = deque()
    visit.append([k,[False]*len(dungeons),0])
    answer = 0
    while visit:
        case = visit.popleft()
        for i in range(len(dungeons)):
            if case[1][i] == False and case[0] >= dungeons[i][0]:
                visited = case[1].copy()
                visited[i] = True
                new_k = case[0] - dungeons[i][1]
                visit.append([new_k,visited,case[2]+1])
                answer = max(answer,case[2]+1)
    return answer
