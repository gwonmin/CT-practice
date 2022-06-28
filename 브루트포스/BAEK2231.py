import sys

I = sys.stdin.readline()

N = int(I)
num = 1
while num <= 1000000:
    sum_num = num
    for i in str(num):
        sum_num += int(i)
    
    if sum_num == N:
        print(num)
        break
    num+=1

if num == 1000001:
    print(0)