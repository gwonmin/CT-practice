'''
크루스칼 알고리즘

최소 신장 트리(Minimum Spanning Tree) 구현에 사용되는 알고리즘으로 가중치 그래프의 모든 간선들을 대상으로
1) 최소 비용의 간선으로 구성
2) 사이클을 형성하지 않음
의 조건을 지켜가며 각 단계마다 사이클을 이루지 않는 최소 비용 간선을 선택하여 최소 신장 트리를 완성하는 알고리즘이다.

프림 알고리즘과 마찬가지로 매 단계마다 최선의 해를 선택하기에 그리디 알고리즘에 바탕을 둔다.

1.그래프의 간선들을 가중치 기준으로 오름차순 정렬한다.
2.정렬된 간선들 중 순서대로 사이클을 형성하지 않는 간선들을 채택한다.
3.선택된 간선을 MST 집합에 넣는다.
4.MST 집합의 원소 개수가 V - 1개가 될 때까지 2, 3을 반복한다.
'''
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
b_lst = list(map(int,input().split()))

mst = set()
visited = set()

info = [list(map(int,input().split())) for _ in range(m)]
info.sort(key= lambda x:x[2])

for i in info:
    if len(mst) < n:
        if i[0] not in visited or i[1] not in visited:
            if b_lst[i[0]-1] > 0 and b_lst[i[1]-1] > 0:
                b_lst[i[0]-1] -= 1
                b_lst[i[1]-1] -= 1
                visited.add(i[0])
                visited.add(i[1])
                mst.add(tuple(i))

if len(mst) != n-1 or n == 1:
    print('NO')
else:
    print('YES')
    for l in mst:
        if l[0] > l[1]:
            print(l[1],l[0])
        else:
            print(l[0],l[1])
