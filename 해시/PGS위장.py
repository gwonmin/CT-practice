clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

def solution(clothes):
    answer = 1
    hash = {}

    for li in clothes:
        # get 메소드는 get(key,x) 로 사용하실 수 있습니다. 이는 '딕셔너리에 key가 없는 경우, x를 리턴해줘라' 라는 용도입니다.
        if(hash.get(li[1],0) == 0):
            hash[li[1]] = 1
        else:
            hash[li[1]] += 1
    
    for i in hash.values():
        answer *= (i+1)
    
    return answer-1