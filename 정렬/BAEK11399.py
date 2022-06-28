n = int(input())
p = list(map(int, input().split()))

p.sort()
result = 0
temp = 0

for i in range(len(p)):
    temp += p[i]
    result += temp

print(result)