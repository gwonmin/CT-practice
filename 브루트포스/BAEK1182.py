from itertools import combinations as combi

N, S = map(int,input().split())

num_lst = list(map(int,input().split()))
result = 0

for i in range(1,N+1):
    all_case = (list(combi(num_lst,i)))
    for case in all_case:
        if sum(case) == S:
            result += 1

print(result)

