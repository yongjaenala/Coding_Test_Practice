def solution(num1, num2):
    if (abs(num1) > 50000) or (abs(num2) > 50000):
        answer = -1
    else:
        answer = num1 + num2

    return answer