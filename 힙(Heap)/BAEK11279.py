import heapq
import sys

input = sys.stdin.readline

N = int(input())

def solution(n):
    arr = []

    for _ in range(n):
        num = int(input())
        if num == 0 and len(arr) == 0:
            print(0)
        elif num == 0:
            print(-heapq.heappop(arr))
        else:
            heapq.heappush(arr,-num)

solution(N)