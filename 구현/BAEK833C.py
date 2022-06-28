'''
from collections import deque
import sys

input = sys.stdin.readline
A, B = map(int,input().split())

def binary(num):
    result = ''
    while num > 1:
        div,mod = divmod(num,2)
        num = div
        result += str(mod)

    result += str(num)
    return result

def XOR(num1,num2):
    lst_len = max(len(num1), len(num2))
    temp1_lst = [0 for _ in range(lst_len)]
    for i in range(len(num1)):
        if num1[i] == '1':
            temp1_lst[i] += 1

    temp2_lst = [0 for _ in range(lst_len)]
    for i in range(len(num2)):
        if num2[i] == '1':
            temp2_lst[i] += 1

    result = 0
    for i in range(lst_len):
        if temp1_lst[i] != temp2_lst[i]:
            result += 2**i

    return result

answer = 0
dq = deque(i for i in range(A,B+1))

while len(dq) != 1:
    a = dq.popleft()
    b = dq.popleft()
    dq.appendleft(XOR(binary(a),binary(b)))

print(dq[0])
'''

import sys

input = sys.stdin.readline
A, B = map(int,input().split())

dp = [A]
for i in range(A+1,B+1):
    dp[0] = dp[0] ^ i

if A == B:
    print(0)
else:
    print(dp[0])