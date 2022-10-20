##### 기초부터 다지기  2022.10.19

# 1. 두 수의 합, 차, 곱, 몫
def solution(num1, num2):
    answer = num1 + num2  # 합
    answer = num1 + num2  # 차
    answer = num1 * num2  # 곱
    answer = num1 // num2  # 몫

    return answer



# 2. 두 수의 나눗셈
import math
def solution(num1, num2):
    answer = math.trunc((num1 / num2) * 1000)

    return answer

# 3. 두 수 비교하기
def solution(num1, num2):
    if (num1 == num2):
        answer = 1
    else:
        answer = -1

    return answer