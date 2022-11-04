# https://school.programmers.co.kr/learn/courses/30/lessons/120912
# 7의 개수

def solution(array):
    answer = 0

    for i in range(len(array)):
        while True:
            if array[i] % 10 == 7:
                answer += 1
            array[i] //= 10
            if array[i] == 0:
                break;

    return answer