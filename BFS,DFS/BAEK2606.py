c = int(input())
n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
result = 0
visited = []

def count(num):
    global graph
    global result
    if num in visited:
        return

    visited.append(num)
    for g in graph:
        if num in g:
            idx = 0 if g.index(num) == 1 else 1
            if g[idx] not in visited:
                result += 1
                count(g[idx])

count(1)
print(result)