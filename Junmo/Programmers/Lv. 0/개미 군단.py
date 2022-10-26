#
# 개미 군단

def solution(hp):
    answer = 0

    while True:
        if hp >= 5:
            hp -= 5
            answer += 1
        elif hp >= 3:
            hp -= 3
            answer += 1
        elif hp >= 1:
            hp -= 1
            answer += 1
        else:
            break;

    return answer