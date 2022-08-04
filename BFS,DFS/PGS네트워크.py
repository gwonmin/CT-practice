n=3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

from collections import deque

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    for c in range(len(computers)):
        for i in range(n):
            if c != i and computers[c][i]:
                graph[c].append(i)

    visited = []
    def bfs(graph,start):
        visit = deque([start])
        visited.append(start)
        while visit:
            idx = visit.popleft()
            for i in graph[idx]:
                if i not in visited:
                    visit.append(i)
                    visited.append(i)

    for i in range(n):
        if i not in visited:
            bfs(graph,i)
            answer += 1

    return answer

print(solution(n,computers))