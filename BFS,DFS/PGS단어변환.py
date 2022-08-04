words = ["hot", "dot", "dog", "lot", "log", "cog"]
# words = ["hot", "dot", "dog", "lot", "log"]
begin = "hit"
target = "cog"

from collections import deque
from collections import defaultdict

def solution(begin, target, words):
    words.append(begin)
    graph = defaultdict()
    if target not in words:
        return 0

    for i in range(len(words)):
        value = []
        for j in range(len(words)):
            temp = 0
            for a,b in zip(words[i],words[j]):
                if a == b:
                    temp += 1
            if temp == len(words[j])-1:
                value.append(words[j])

        graph[words[i]] = value

    visited = []
    def bfs(graph, start):
        visit = deque()
        visit.append([start])
        count = 0

        while visit:
            v_lst = visit.popleft()
            count += 1
            for v in v_lst:
                if graph[v] not in visited:
                    visit.append(graph[v])
                    visited.append(graph[v])

            if target in visited[-1]:
                return count

        return 0
    return bfs(graph,begin)

print(solution(begin, target, words))