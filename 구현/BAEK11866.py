from collections import deque

N, K = map(int,input().split())

dq = deque([i for i in range(1,N+1)])
result = []

while dq:
    for _ in range(K-1):
        dq.append(dq.popleft())

    result.append(dq.popleft())

print(str(result).replace('[','<').replace(']','>'))
