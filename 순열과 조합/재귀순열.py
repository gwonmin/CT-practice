def permutation(arr, r):
    
    # 순열을 저장할 배열
    result = []
    
    # 실제 순열을 구하는 함수
    def permute(p, index):
        if len(p) == r:
            result.append(p)
            return

        for idx, data in enumerate(arr):
            print(p, data, index, idx)
            if idx not in index: 
				# list는 mutable이기 때문에 새로운 리스트를 넘겨준다.
            	permute(p + [data], index + [idx]) #재귀
	
    permute([], [])
    
    return result

for r in permutation(['A', 'B', 'C', 'D'], 2):
    print(r)