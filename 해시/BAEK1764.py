N,M = map(int,input().split())

set_one = set(input() for _ in range(N))
set_two = set(input() for _ in range(M))

result_set = set_one.intersection(set_two)
result_lst = list(result_set)
result_lst.sort()

print(len(result_lst))
for i in range(len(result_lst)):
    print(result_lst[i])
