import sys

input = sys.stdin.readline
n = int(input())

meet = [list(map(int,input().split())) for _ in range(n)]
meet.sort(key = lambda x : (x[1],x[0]))

end = 0
count = 0

for m in meet:
    if end <= m[0]:
        end = m[1]
        count += 1

print(count)
