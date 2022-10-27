# https://school.programmers.co.kr/learn/courses/30/lessons/120839
# 가위 바위 보

def solution(rsp):
    answer = ''

    for h in rsp:
        if h == '0':
            answer += '5'
        elif h == '2':
            answer += '0'
        else:
            answer += '2'

    return answer