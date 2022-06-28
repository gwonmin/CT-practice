# sum()

# result = sum( [1, 2, 3, 4, 5] )
# print(result) => 15

# min()

# result = min(7, 3, 6, 1)
# print(result) => 1
# max()
# result = max(7, 3, 6, 1)
# print(result) => 7

# eval() : 수학 수식(문자열 형태) 계산 결과 반환

# result = eval("(3+5) * 7")
# print(result) => 56

#sorted()

# result = sorted([4, 7, 3, 1])  # 오름 차순
# print(result) => [1,3,4,7]
# result = sorted([4, 7, 3, 1], reverse = True) # 내림차순
# print(result) => [7,4,3,1]

# x[1] 을 기준으로 했으므로 숫자들 기준으로 내림차순 정렬됨
# result = sorted( [ ('a', 40), ('b', 70), ('c', 20) ] , key = lambda x : x[1], reverse = True)
# print(result) => [ ('b', 70), ('a', 40) ,('c', 20) ]

# 리스트와 같은 iterable 객체는 기본적으로 sort() 함수 내장!
# 굳이 sorted() 안 써도 됨 => 리스트 값이 정렬된 것으로 바로 바뀜

# data = [3, 1, 2]
# data.sort()
# print(data) => [1, 2, 3]

