import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0, 1]
    def fibo(n):

        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            global dp
            if len(dp) > n:
                return dp[n]
            else:
                t = fibo(n-1) + fibo(n-2)
                dp.append(t)
                return t

    if N == 0:
        print(1,0)
    elif N == 1:
        print(0,1)
    else:
        fibo(N)
        print(dp[-2], dp[-1])
