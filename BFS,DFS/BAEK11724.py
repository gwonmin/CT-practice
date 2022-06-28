import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())

visited = []
graph = [list(map(int,input().split())) for _ in range(M)]
result = 0

def visit(num):
    global graph
    if num in visited:
        return

    visited.append(num)
    for g in graph:
        if num in g:
            idx = g.index(num)
            another_idx = 0 if idx == 1 else 1
            if g[another_idx] not in visited:
                visit(g[another_idx])

for i in range(1,N+1):
    if i not in visited:
        visit(i)
        result += 1

print(result)