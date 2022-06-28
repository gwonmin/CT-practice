from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())

num_lst = [int(input()) for _ in range(N)]
num_lst.sort()

count = Counter(num_lst)
most_count = [i for i in count if max(count.values())==count[i]]

print(round(sum(num_lst)/N))
print(num_lst[len(num_lst)//2])
print(most_count[0] if len(most_count) == 1 else most_count[1])
print(max(num_lst)-min(num_lst))

