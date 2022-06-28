# PriorityQueue 보다 빠름.

# 원소 삽입: heapq.heappush()
# 원소 꺼냄: heapq.heappop()

# 기본 최소 힙 코드)

# import heapq
# def heapsort(iterable):
#     h=[]
#     result =[]
    
#     #모든 원소 차례로 힙에 삽입
#     for value in iterable:
#         heapq.heappush(h,value); # h 에 value 를 push
    
#     # 힙의 모든 원소 꺼내기
#     for i in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result
# result = heapsort([2,1,3,0,5,4])
# print(result) # [0,1,2,3,4,5] 최소힙 - 오름차순 정렬
        

# 최대 힙 구현 코드) -> 값에 -를 붙여서 넣는다!

# import heapq

# def heapsort(iterable):
#     h=[]
#     result =[]
    
#     #모든 원소 차례로 힙에 삽입
#     for value in iterable:
#         heapq.heappush(h,-value); # 원소에 - 를 붙여 넣으면 반대로 됨!
    
#     # 힙의 모든 원소 꺼내기
#     for i in range(len(h)):
#         result.append(-heapq.heappop()) # 다시 원소에 - 붙이기
#     return result
# result = heapsort([2,1,3,0,5,4])
# print(result) # [5,4,3,2,1,0] 최소힙 - 오름차순 정렬