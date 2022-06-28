import heapq

def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        target_list = array[i-1:j]
        heap = []
        
        for i in target_list:
            heapq.heappush(heap,i)
        
        sorted_heap = []
        for i in range(len(heap)):
            sorted_heap.append(heapq.heappop(heap))
        
        answer.append(sorted_heap[k-1])
    
    return answer