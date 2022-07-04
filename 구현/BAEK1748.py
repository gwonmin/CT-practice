import sys

input = sys.stdin.readline
N = int(input())

result = 0
temp = '9'

for i in range(1,len(str(N))+1):
    if N > int(temp):
        N -= int(temp)
        result += int(temp)*i
    elif N <= int(temp):
        result += N*i
    temp += '0'

print(result)
'''
1 1~9
2 10~99
3 100~999
4 1000~9999
'''