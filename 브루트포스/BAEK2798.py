from itertools import permutations
import sys
import bisect

I = sys.stdin.readline()
num_list = I.split(' ')
N = int(num_list[0])
M = int(num_list[1])

card = sys.stdin.readline().strip()
card_list = card.split(' ')

case = (list(permutations(map(int,card_list), 3)))
sum_case = [sum(i) for i in case]
sum_case.sort()
lower_idx = bisect.bisect_left(sum_case, M)-1

if M in sum_case:
    result = M
else:
    result = sum_case[lower_idx]

print(result)

