def solution(answers):
    answer = []
    supoA = [1,2,3,4,5] 
    supoB = [2,1,2,3,2,4,2,5]
    supoC = [3,3,1,1,2,2,4,4,5,5] 
    scoreList = [0, 0, 0]
    
    for i in range(len(answers)):
        if supoA[i%len(supoA)] == answers[i]:
            scoreList[0] += 1
            
        if supoB[i%len(supoB)] == answers[i]:
            scoreList[1] += 1
            
        if supoC[i%len(supoC)] == answers[i]:
            scoreList[2] += 1
        
    maxScore = max(scoreList)
    
    for i in range(len(scoreList)):
        if scoreList[i] == maxScore:
            answer.append(i+1)
        
    return answer