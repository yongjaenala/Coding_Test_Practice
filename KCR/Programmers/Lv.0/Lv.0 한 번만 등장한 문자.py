def solution(s):
    a = {}
    for i in s :
        if i not in a.keys() :
            a[i] = 1
        else :
             a[i] += 1
    a = dict(sorted(a.items()))
    answer = ''
    for i, j in enumerate(a.values()) :
        if j == 1 :
            answer += list(a.keys())[i]
    return answer