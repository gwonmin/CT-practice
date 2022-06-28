import sys
N = int(sys.stdin.readline())
#형변환 주의
case = [list(map(int,sys.stdin.readline().strip().split( ))) for i in range(N)]
result = []

for i in range(len(case)):
    k=0
    for j in range(len(case)):
        if case[i][0] < case[j][0] and case[i][1] < case[j][1]:
            k += 1
    result.append(k+1)
print(" ".join(map(str,result)))
