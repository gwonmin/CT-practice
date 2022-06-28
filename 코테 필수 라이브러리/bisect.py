# '정리된 배열'에서 특정한 원소 찾을때 매우 효과적!

# bisect_left(), bisect_right() 함수가 가장 중요, 둘다 시간복잡도 O(logN)

# - bisect_left(a,x) : 정렬 순서 유지, 리스트 a에 데이터 x를 삽입 할 가장 왼쪽 인덱스 찾음
# - bisect_right(a,x): 정렬 순서 유지, 리스트 a에 데이터 x를 삽입 할 가장 오른쪽 인덱스 찾음

# from bisect import bisect_left, bisect_right
# a=[1,2,4,4,8]
# x=4
# print(bisect_left(a,x) => 2
# print(bisect_right(a,x) =>4

# bisect_left(), bisect_right() : ' 정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수' 구할때 효과적!!

# from bisect import bisect_left, bisect_right

# def count(a, left_value, right_value):
#     left_index = bisect_left(a, left_value)
#     right_index = bisect_right(a, right_value)
#    return right_index - left_index

# a=[1,2,3,3,3,3,4,5]
# a 리스트에서 값이 3인 데이터의 갯수 
# print(count(a,3,3)) # 답:4
# a 리스트에서 [-1,3] 범위에 있는 데이터의 갯수
# print(count(a,-1,3)) # 답:6


