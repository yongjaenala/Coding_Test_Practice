def solution(array, n):
    answer = {}
    for i in array :
        if i in answer.keys() :
            answer[i] += 1
        else :
            answer[i] = 1
    if n in array :
        return answer[n]
    else :
        return 0