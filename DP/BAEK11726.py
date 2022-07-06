n = int(input())

def solution(n):
    # 경우의 수
    dp = [1, 2]
    target_idx = 2

    if n == 1:
        return 1

    while n != target_idx:
        dp.append(dp[target_idx-2]+dp[target_idx-1])
        target_idx += 1

    return dp[-1]

print(solution(n)%10007)
