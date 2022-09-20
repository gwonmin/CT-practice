import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_lst = [i for i in range(1,n+1)]

def dfs(lst):
    if len(lst) == m:
        print(str(lst).replace('[','').replace(']','').replace(',',''))
        return

    for n in n_lst:
        if lst + [n] == sorted(lst + [n]):
            dfs(lst + [n])

dfs([])