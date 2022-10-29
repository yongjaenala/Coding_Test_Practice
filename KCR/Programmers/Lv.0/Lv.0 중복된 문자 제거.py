def solution(my_string):
    s = {}
    for i in my_string :
        if i not in s.keys() :
            s[i] = 1
    answer = ''
    for i in s.keys() :
        answer += i
    return answer