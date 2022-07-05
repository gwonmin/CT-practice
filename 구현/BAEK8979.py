N, K = map(int, input().split())

medal = [list(map(int,input().split())) for _ in range(N)]

for m in medal:
    if m[0] == K:
        target = m[1:]
        break

result = sorted(medal,key=lambda x: (x[1],x[2],x[3]), reverse= True)

rank = 0
for i in range(len(result)):
    rank += 1
    if result[i][1:] == target:
        break

print(rank)