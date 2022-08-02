
#1'
# def solution(numbers):
#     answer = 0
#     case = [num for num in numbers]
#     numSet = set()
#     for i in range(1,len(numbers)+1):
#         for r in permutation(case, i):
#             numSet.add(int("".join(r)))
#
#     for i in numSet:
#         if sosu(i):
#             answer += 1
#
#     return answer
#
# def permutation(arr, r):
#     # 순열을 저장할 배열
#     result = []
#     # 실제 순열을 구하는 함수
#     def permute(p, index):
#         if len(p) == r:
#             result.append(p)
#             return
#         for idx, data in enumerate(arr):
#             if idx not in index:
# 				# list는 mutable이기 때문에 새로운 리스트를 넘겨준다.
#             	permute(p + [data], index + [idx])
#
#     permute([], [])
#     return result
#
#
# def sosu(number):
#     if number == 1:
#         return False
#     elif number == 0:
#         return False
#
#     for i in range(2,number):
#         if number % i == 0:
#             return False
#     return True

#2
from itertools import permutations
import math

numbers = '17'
def solution(numbers):
    answer = 0
    case_set = set()
    for i in range(1,len(numbers)+1):
        for permu in permutations(numbers,i):
            number = int(''.join(permu))
            case_set.add(number)
    for case in case_set:
        if sosu(case):
            answer += 1
    return answer

def sosu(number):
    if number == 1:
        return False
    if number == 0:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

print(solution(numbers))


