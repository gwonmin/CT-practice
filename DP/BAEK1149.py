N = int(input())

cache =[list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    cache[i][0] += min(cache[i-1][1], cache[i-1][2])
    cache[i][1] += min(cache[i-1][0], cache[i-1][2])
    cache[i][2] += min(cache[i-1][0], cache[i-1][1])

print(min(cache[-1]))