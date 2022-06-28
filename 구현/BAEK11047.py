N, K = map(int, input().split())

coin = []
result = 0

for _ in range(N):
    coin.append(int(input()))

for i in range(N - 1, -1, -1):
    if coin[i] <= K:
        a, b = divmod(K,coin[i])
        K = b
        result += a

print(result)

