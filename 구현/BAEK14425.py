from collections import Counter

N, M = map(int, input().split())

N_lst = [input() for _ in range(N)]

count_dict = Counter(input() for _ in range(M))

result = 0

for i in N_lst:
    result += count_dict[i]

print(result)