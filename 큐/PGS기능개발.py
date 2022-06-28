from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    progress_queue = deque(progresses)
    speeds_queue = deque(speeds)
    
    finish = 0
    while progress_queue:
        day = math.ceil((100-progress_queue.popleft())/speeds_queue.popleft())
        finish += 1
        while True:
            if len(progress_queue) == 0:
                break
            if math.ceil((100-progress_queue[0])/speeds_queue[0]) <= day:
                progress_queue.popleft()
                speeds_queue.popleft()
                finish += 1
            else:
                break
        
        answer.append(finish)
        finish = 0
    
    return answer