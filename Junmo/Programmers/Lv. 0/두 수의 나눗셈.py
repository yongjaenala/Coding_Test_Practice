# 두 수의 나눗셈
# num1을 num2로 나눈 뒤 1000을 곱한 수에 정수 부분만 출력

def solution(num1, num2):
    answer = 0

    answer = int(num1 / num2 * 1000)    # int는 내림함 (소수점 버림)

    return answer