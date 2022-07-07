import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
graph[0] = [0,0]
visited = [False for _ in range(N+1)]

count = 0

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

def DFS(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)

#1부터 탐색하며 visited[i]가 False 이면 연결요소가 하나 더 있다는 의미
#연결요소가 더이상 없을 경우 visted 내의 모든 요소가 True가 되야함
for i in range(1, len(visited)):
    print(visited)
    if visited[i] == False:
        count += 1
        DFS(graph, i, visited)

print(count)