N = int(input())
count = [[] for _ in range(51)]

for _ in range(N):
    s = input()
    idx = len(s)
    if s in count[idx]:
        pass
    else:
        count[idx] += [s]

for i in range(len(count)):
    count[i].sort()
    for c in count[i]:
        print(c)