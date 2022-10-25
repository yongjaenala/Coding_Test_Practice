# https://school.programmers.co.kr/learn/courses/30/lessons/120851
# 숨어있는 숫자의 덧셈 (1)

def solution(my_string):
    answer = 0

    for val in my_string:
        try:
            if int(val) >= 0:
                answer += int(val)
        except:
            pass

    return answer