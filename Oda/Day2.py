### 기초 다지기  DAY 2  2022.10.21

# 분수의 덧셈
import math

def solution(denum1, num1, denum2, num2):
    bottom = num1 * num2
    top = ((denum1 * num2) + (denum2 * num1))

    b = bottom / math.gcd(bottom, top)
    t = top / math.gcd(bottom, top)

    answer = [t, b]
    return answer


# 배열 원소 값 두배 만들기
def solution(numbers):
    answer = []

    for i in numbers:
        answer.append(i * 2)

    return answer

# 나머지 구하기
def solution(num1, num2):
    answer = num1 % num2

    return answer

# 중앙값 구하기

import math


def solution(array):
    array.sort()

    if (len(array) % 2 == 0):
        n = len(array)
        answer = (array[n] + array[n + 1]) / 2
    else:
        n = len(array)
        i = math.trunc(n / 2)
        answer = array[i]

    return answer