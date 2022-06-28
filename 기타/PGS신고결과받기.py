from collections import Counter

def solution(id_list, report, k):
    answer = []
    report = set(report)
    total_dict = {key : [] for key in id_list}        
    value_list = []
    ban_list = []
    
    for i in report:
        key, value = i.split()
        total_dict[key] = total_dict[key] + [value]
        value_list.append(value)
        
    value_dict = dict(Counter(value_list))
    
    for key in value_dict:
        if value_dict[key] >= k:
            ban_list.append(key)
            
    for key in total_dict:
        result = 0
        for value in total_dict[key]:
            if value in ban_list:
                result += 1
        answer.append(result)
    
    return answer