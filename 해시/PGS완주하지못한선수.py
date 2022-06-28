participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    dict = {}

    for i in participant:
        if(i in dict):
            dict[i] += 1
        else:
            dict[i] = 1

    for i in completion:
        dict[i] -= 1

    for i in dict:
        if(dict[i] == 1):
            return i
    

print(solution(participant, completion))