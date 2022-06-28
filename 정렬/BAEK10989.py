#계수정렬
import sys
input = sys.stdin.readline

N = int(input())
num_lst = [0 for _ in range(10001)]

for _ in range(N):
    num = int(input())
    num_lst[num] += 1

for i in range(1,len(num_lst)):
    for _ in range(num_lst[i]):
        print(i)



#시간초과
'''import bisect
import sys

input = sys.stdin.readline
N = int(input())
result = []

for _ in range(N):
    num = int(input())
    idx = bisect.bisect_right(result,num)
    result.insert(idx,num)

for r in result:
    print(r)
'''