import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

ground = [list(map(int,input().split())) for _ in range(N)]

result = []

for h in range(257):
    time = 0
    block = B
    for n in range(len(ground)):
        for m in range(len(ground[n])):
            if h > ground[n][m]:
                block -= h-ground[n][m]
                time += (h-ground[n][m])
            elif h < ground[n][m]:
                block += ground[n][m]-h
                time += (ground[n][m]-h)*2

    if block >= 0:
        result.append([time,h])
    else:
        break

result = sorted(result, key = lambda x: (x[0],-x[1]))
print(str(result[0]).replace('[','').replace(',','').replace(']',''))
