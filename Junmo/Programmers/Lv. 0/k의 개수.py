# https://school.programmers.co.kr/learn/courses/30/lessons/120887
# k의 개수

def solution(i, j, k):
    answer = 0

    temp = 0
    for num in range(i, j + 1):
        temp = num
        while temp:
            if temp % 10 != k:
                temp //= 10
            else:
                answer += 1
                temp //= 10

    return answer