from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    info = defaultdict(list)
    for _ in range(n):
        value, key = input().split()
        info[key] += [value]

    case = [len(lst) for lst in info.values()]
    result = 1
    for c in case:
        result *= c+1
    print(result-1)