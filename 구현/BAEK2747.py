n = int(input())

fibo = [0, 1]+[0]*n

for i in range(2,len(fibo)):
    fibo[i] = fibo[i-2] + fibo[i-1]

print(fibo[n])
