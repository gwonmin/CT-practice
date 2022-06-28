N = int(input())
xy_lst = []

for _ in range(N):
    xy = list(map(int,input().split()))
    xy_lst.append(xy)

xy_lst.sort(key=lambda x:(x[1],x[0]))

for xy in xy_lst:
    print(xy[0], xy[1])