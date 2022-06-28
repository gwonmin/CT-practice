
N, M = map(int,input().split())

board = [list(input()) for _ in range(N)]

W_case = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

B_case = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]



def check(case):
    global W_case
    global B_case

    w = 0
    b = 0

    for i in range(len(case)):
        for j in range(len(case[i])):
            if case[i][j] != W_case[i][j]:
                w += 1
            elif case[i][j] != B_case[i][j]:
                b += 1

    min_val = min(w,b)
    return min_val

result = 1000000

for i in range(N-7):
    for j in range(M-7):
        case = [[board[b+i][a+j] for a in range(8)] for b in range(8)]
        result = min(result,check(case))

print(result)