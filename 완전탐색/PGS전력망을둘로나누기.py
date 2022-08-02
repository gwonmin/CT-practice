#내 풀이
from collections import deque
n=9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

def solution(n, wires):
    answer = 99999999999999

    def bfs(wire,wires,visited):
        count = 1
        visit = deque()
        visit.append(wire)
        while visit:
            case = visit.popleft()
            for i in range(len(wires)):
                if case[0] in wires[i] and wires[i] not in visited:
                    visited.append(wires[i])
                    visit.append(wires[i])
                    count += 1
                if case[1] in wires[i] and wires[i] not in visited:
                    visited.append(wires[i])
                    visit.append(wires[i])
                    count += 1
        return count

    for i in range(len(wires)):
        new_wires = wires.copy()
        new_wires.pop(i)
        visited = []
        result_lst = []
        for j in range(len(new_wires)):
            if new_wires[j] not in visited:
                result_lst.append(bfs(new_wires[j],new_wires,visited))
            if len(visited) == len(new_wires):
                break

        if len(result_lst) == 2:
            answer = min(answer,abs(result_lst[0]-result_lst[1]))
        else:
            answer = min(answer,result_lst[0]-1)
    return answer

print('my',solution(n,wires))

#모범 답안
from collections import deque
def solution(n, wires):
    answer = int(1e9)
    graph = [[] for _ in range(n+1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start):
        visited[start] = True
        visit = deque([start])
        count = 0
        while visit:
            case = visit.popleft()
            count += 1
            for node in graph[case]:
                if not visited[node] and [min(case, node), max(case, node)] != del_edge:
                    visit.append(node)
                    visited[node] = True
        return count

    for a,b in wires:
        del_edge = [a, b]
        visited = [False] * (n+1)
        A = bfs(1)
        B = 0
        for i in range(1, n+1):
            if not visited[i]:
                B = bfs(i)
                break
        answer = min(answer, abs(A - B))

    return answer

print(solution(n,wires))
