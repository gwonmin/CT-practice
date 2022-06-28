N = int(input())
info = [input().split() for _ in range(N)]
info = list(map(lambda x: [int(x[0]),x[1]],info))
info = sorted(info, key=lambda x: x[0])

for i in info:
    print(i[0],i[1])
