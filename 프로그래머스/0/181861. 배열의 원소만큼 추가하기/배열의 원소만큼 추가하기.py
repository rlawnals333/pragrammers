def solution(arr):
    
    answer = []
    
    for j in arr:
        for i in range(j):
            answer.append(j)
    
    return answer