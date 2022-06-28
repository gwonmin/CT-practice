from collections import defaultdict

N = int(input())
N_lst = list(map(int,input().split()))

N_dict = defaultdict(int)

for n in N_lst:
    N_dict[n] += 1

M = int(input())
result_lst = [N_dict[m] for m in list(map(int,input().split()))]

print(str(result_lst).replace('[','').replace(']','').replace(',',''))