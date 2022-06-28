N = int(input())
idx_lst = [[] for _ in range(200001)]

for _ in range(N):
    xy = list(map(int,input().split()))
    idx = xy[0]+100000
    idx_lst[idx] += [xy]

for i in range(len(idx_lst)):
    if len(idx_lst[i]) == 0:
        pass
    else:
        sorted_y = sorted(idx_lst[i],key=lambda x:x[1])
        for result in sorted_y:
            print(result[0], result[1])