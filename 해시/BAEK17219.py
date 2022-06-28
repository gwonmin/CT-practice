from collections import defaultdict
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

info_dict = defaultdict(str)

for _ in range(N):
    key, value = input().strip().split()
    info_dict[key] = value

for _ in range(M):
    key = input().strip()
    print(info_dict[key])
