from collections import Counter
import math

N = input()

if '6' in N:
    N = N.replace('6','9')

N_lst = list(N)

count = 0
count_dict = Counter(N_lst)

m_num = max(count_dict)

if m_num == '6' or m_num == '9':
    count_dict[m_num] = math.ceil((count_dict[m_num] / 2))

key = max(count_dict, key = count_dict.get)
print(count_dict[key])