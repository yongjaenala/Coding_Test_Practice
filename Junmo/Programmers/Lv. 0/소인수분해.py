# https://school.programmers.co.kr/learn/courses/30/lessons/120852
# 소인수분해

def solution(n):
    answer = []

    for i in range(2, n + 1):
        if n % i == 0:
            temp = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    temp += 1
            if temp == 2:
                answer.append(i)

    return answer