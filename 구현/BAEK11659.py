import sys
input = sys.stdin.readline

N, M = map(int,input().split())

N_lst = [0]+list(map(int,input().split()))

sum = 0
sum_lst = []

for n in N_lst:
    sum += n
    sum_lst.append(sum)

for _ in range(M):
    i,j = map(int,input().split())
    print(sum_lst[j]-sum_lst[i-1])
