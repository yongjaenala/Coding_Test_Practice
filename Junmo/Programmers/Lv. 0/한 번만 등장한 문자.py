# https://school.programmers.co.kr/learn/courses/30/lessons/120896
# 한 번만 등장한 문자

def solution(s):
    answer = ''

    temp = dict()
    for s in s:
        if temp.get(s):
            temp[s] += 1
        else:
            temp[s] = 1
    temp = sorted(temp.items())
    temp = dict(temp)
    for k, v in temp.items():
        if v == 1:
            answer += k

    return answer