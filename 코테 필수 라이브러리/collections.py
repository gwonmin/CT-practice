# 1. deque : 보통 큐 구현 할 때 사용!! (스택도 가능, Queue 라이브러리보다 빠름)
# - list 는 삭제, 삽입이 모두 '가장 뒤쪽 원소' 기준임!
# - but, deque 이용시 popleft()로 첫번째 원소 삭제, append(x)로 마지막 인덱스에 삽입함
#                           (pop()으로 마지막 원소 삭제, appendleft(x)로 첫번째 인덱스에 삽입 가능)

# from collections import deque
# data = deque([2,3,4])
# data.appendleft(1)
# data.append(5)

# print(data) # deque([1,2,3,4,5])
# print(list(data)) # [1,2,3,4,5] 리스트 자료형으로 변환


# 2. Counter: 등장 횟수 셈! 
# 리스트 같은 iterable 객체에서, 내부 원소가 몇번씩 등장했는지 알려줌.

# from collections import Counter
# counter = Counter(['r','b','r','b','g','b'])

# print(counter['b']) # 'b' 등장횟수, 답: 3
# print(counter['g'] # 1
# print(dict(counter)) # {'r':2, 'b':3, 'g':1}
