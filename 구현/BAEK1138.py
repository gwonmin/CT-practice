N = int(input())
case = list(map(int,input().split()))

result = [0 for _ in range(N)]

for i in range(N):
    room = case[i]
    for j in range(len(result)):
        if room == 0 and result[j] == 0:
            result[j] = i+1
            break
        elif result[j] == 0:
            room -= 1

print(' '.join(map(str,result)))