from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) # sum, level
    print(queue)
    while queue:
        s, l = queue.popleft()
        print(s, l)
        if l > len(numbers):
            break
        elif l == len(numbers) and s == target:
            answer += 1
        queue.append((s+numbers[l-1], l+1))
        queue.append((s-numbers[l-1], l+1))
        print(queue)

    return answer

solution([4, 1, 2, 1],4)

# 재귀 조합 완전탐색 활용 : 시간초과!
# def solution(numbers, target):
#     answer = 0
#     idxList = list(range(len(numbers)))
    
#     for i in range(len(numbers)+1):
#         caseList = permutation(idxList,i)
#         for case in caseList:
#             numberSum = sum(numbers)
            
#             for idx in case:
#                 numberSum -= numbers[idx]*2
                
#             if numberSum == target:
#                 answer += 1
                
#     return answer

# #재귀 조합
# def permutation(arr, r):
#     result = []
    
#     def permute(case,idx):
#         if(len(case) == r):
#             result.append(case)
#             return
#         for index, data in enumerate(arr):
#             if index > idx:
#                 permute(case+[data], index)
            
#     permute([],-1)
#     return result