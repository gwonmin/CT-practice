from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())

    lst = deque([idx,imp] for idx,imp in enumerate(map(int,input().split())))

    count = 1
    while True:
        max_imp = max(lst,key=lambda x:x[1])[1]
        if lst[0][1] >= max_imp:
            if lst.popleft()[0] == M:
                print(count)
                break
            else:
                count += 1
        else:
            lst.append(lst.popleft())
