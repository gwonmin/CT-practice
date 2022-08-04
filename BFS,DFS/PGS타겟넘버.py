numbers=[4, 1, 2, 1]
target = 4
#조합 풀이
# from itertools import combinations
#
# def solution(numbers, target):
#     answer = 0
#     idx_lst = [i for i in range(len(numbers))]
#     for i in range(1,len(idx_lst)+1):
#         combi = combinations(idx_lst,i)
#         for c in combi:
#             sum_num = 0
#             for idx in range(len(numbers)):
#                 if idx in c:
#                     sum_num -= numbers[idx]
#                 else:
#                     sum_num += numbers[idx]
#             if sum_num == target:
#                 answer += 1
#     return answer

# print(solution(numbers,target))

#dfs recursive
#
# def solution(numbers, target):
#     def dfs(pos, cur):
#         if pos == len(numbers):
#             return cur == 0
#         return dfs(pos + 1, cur + numbers[pos]) + dfs(pos + 1, cur - numbers[pos])
#     return dfs(0, target)
#
# print(solution(numbers,target))

# def solution(numbers, target):
#
#     def DFS(numbers, target, depth):
#         answer = 0
#         if depth == len(numbers):
#             return sum(numbers) == target
#         else:
#             answer += DFS(numbers, target, depth+1)
#             numbers[depth] *= -1
#             answer += DFS(numbers, target, depth+1)
#             return answer
#
#     answer = DFS(numbers, target, 0)
#     return answer

#dfs stack
#
# def solution(numbers, target):
#     answer = 0
#     stack = [(0,0)]
#     while stack:
#         idx,sum_num = stack.pop()
#         if idx == len(numbers):
#             answer += (sum_num == target) #True면 1
#         else:
#             stack.append((idx+1,sum_num+numbers[idx]))
#             stack.append((idx+1,sum_num-numbers[idx]))
#     return answer
#
# print(solution(numbers,target))

# # bfs
# def solution(numbers, target):
#     answer = 0
#     leaves = [0]
#     for num in numbers:
#         tmp = []
#         for parent in leaves:
#             tmp.append(parent + num)
#             tmp.append(parent - num)
#         leaves = tmp
#     for leaf in leaves:
#         if leaf == target:
#             answer += 1
#     return answer

def solution(numbers, target):
    answer = 0
    stack = [(0,0)]
    while stack:
        depth, sum_num = stack.pop()
        if depth == len(numbers):
            answer += (target == sum_num)
        else:
            stack.append((depth+1,sum_num+numbers[depth]))
            stack.append((depth+1,sum_num-numbers[depth]))
    return answer

print(solution(numbers,target))