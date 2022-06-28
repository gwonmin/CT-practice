facto = 1
for i in range(int(input()),0,-1):
    facto *= i

result = 0
for n in list(str(facto))[::-1]:
    if n == '0':
        result += 1
    else:
        break

print(result)