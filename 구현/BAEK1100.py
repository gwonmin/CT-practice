s_w = ''
s_b = ''

for i in range(8):
    if i % 2 == 0:
        s_w += input()
    else:
        s_b += input()

result = 0
for i in range(0,len(s_w),2):
    if s_w[i] == 'F':
        result += 1

for i in range(1,len(s_b),2):
    if s_b[i] == 'F':
        result += 1

print(result)