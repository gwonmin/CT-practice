import sys

input = sys.stdin.readline

n = int(input())

stair = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n+1)]

print(stair)