# https://school.programmers.co.kr/learn/courses/30/lessons/120905
# n의 배수 고르기

def solution(n, numlist):
    answer = []

    for num in numlist:
        if num % n == 0:
            answer.append(num)

    return answer