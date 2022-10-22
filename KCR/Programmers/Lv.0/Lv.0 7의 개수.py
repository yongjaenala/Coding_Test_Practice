def solution(array):
    answer = 0
    for i in array:
        if '7' in str(i) :
            answer += str(i).count('7') # 7 -> 1 ; 77 -> 2
    return answer