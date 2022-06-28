#set() 탐색의 시간복잡도는 O(1)
#list() 는 O(N)

import sys
input = sys.stdin.readline
N = int(input())
num_lst = set(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))

for i in m_lst:
    if i in num_lst:
        print(1)
    else:
        print(0)

