#수학적 풀이
def solution(brown, yellow):
    x = 0
    y = 3
    while True:
        if 2*((yellow+brown)/y+y) == (brown+4):
            break
        else:
            y += 1
    
    x = (yellow+brown)/y
    
    answer = [x, y]
    
    return answer