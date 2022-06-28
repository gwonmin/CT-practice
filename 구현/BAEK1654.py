#이분탐색
k, n = map(int, input().split())

lines = [int(input()) for _ in range(k)]

start = 1
end = max(lines)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(k):
        cnt += lines[i] // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)