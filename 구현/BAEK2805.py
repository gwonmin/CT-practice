#이분탐색
import sys

input = sys.stdin.readline
N, M = map(int,input().split())

trees = list(map(int,input().split()))

start = 1
end = max(trees)

while start <= end:
    target = 0
    mid = (start + end) // 2

    for i in range(N):
        if trees[i] > mid:
            target += trees[i] - mid

    if target >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)