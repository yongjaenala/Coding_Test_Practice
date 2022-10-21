import math


def solution(denum1, num1, denum2, num2):
    son = denum1 * num2 + denum2 * num1
    mom = num1 * num2

    gcd = math.gcd(son, mom)

    if gcd != 1:
        son = son // gcd
        mom = mom // gcd

    answer = [son, mom]

    return answer