sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    max_len = 0
    min_len = 0
    for size in sizes:
        max_len = max(max_len,max(size))
        min_len = max(min_len,min(size))

    answer = max_len * min_len
    return answer

print(solution(sizes))