

# 1. permutations: 리스트 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)제시

#                       클래스이므로 객체 초기화 후 리스트 자료형으로 변환 해야함.

# from itertools import permutations
# data = ['A', 'B', 'C']
# result = list(permutations(data, 3)) # 데이터중 3개를 뽑아 나열(순열)
# print(result) => [('A', 'B' ,'C'),('A', 'C', 'B'), ,,,,,,,, , ('C', 'B', 'A')]

# 2. combinations: 리스트 같은 iterable 객체에서 r개의 데이터를 뽑아 순서없이 일렬로 나열하는 모든 경우(조합) 제시

#                       클래스이므로 객체 초기화 후 리스트 자료형으로 변환 해야함.

# from itertools import combinations
# data = ['A', 'B', 'C']
# result = list(combinations(data, 2)) # 데이터중 2개를 뽑아 순서없이 나열(조합)
# print(result) => [('A', 'B'), ('A', 'C'),  ('B', 'C')]

# 3. product:  permutations에서 원소 중복, 뽑고자 하는 데이터 수를 repeat 속성값으로 넣음

# from itertools import product
# data = ['A', 'B', 'C']
# result = list(product(data, repeat=2)) # 데이터중 2개를 뽑아 나열(중복 순열)
# print(result) => [('A', 'A'),('A', 'B'), ,,,,,,,, , ('C', 'C')] => 9개나옴

# 4. combinations_with_replacement: combinations 에서 중복 허용

# from itertools import combinations_with_replacement
# data = ['A', 'B', 'C']
# result = list(combinations_with_replacement(data, 2)) # 데이터중 2개를 뽑아 순서없이 나열(중복 조합)
# print(result) => [('A', 'A'),('A', 'B'), ,,,,,,,, , ('C', 'C')] =>6개 나옴