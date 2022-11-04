def solution(hp):
    cnt = 0
    cnt += hp // 5
    na = hp - ((hp // 5) * 5)
    cnt += na // 3
    na = na - ((na // 3) * 3)
    cnt += na // 1

    return cnt



def solution1(hp):
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)

def solution2(hp):
    answer = 0
    answer += hp//5
    hp %= 5
    answer += hp//3
    hp %= 3
    answer += hp//1

    return answer