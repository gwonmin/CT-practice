r = 31
M = 1234567891

L = int(input())
s = input()

alpha_dict = {chr(i):i-96 for i in range(97,123)}
result = 0

for i in range(len(s)):
    result += alpha_dict[s[i]]*(r**(i))

print(result%M)