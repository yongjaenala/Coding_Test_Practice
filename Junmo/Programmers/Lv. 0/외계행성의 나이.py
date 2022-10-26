# https://school.programmers.co.kr/learn/courses/30/lessons/120834
# 외계행성의 나이

def solution(age):
    answer = ''

    ageNum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    while True:
        if age == 1000:
            answer = "baaa"
            break;
        elif age == 100:
            answer = "baa"
            break;
        elif age == 10:
            answer = "ba"
            break;
        elif age > 100:
            answer += ageNum[age // 100]
            age = age % 100
        elif age > 10:
            answer += ageNum[age // 10]
            age = age % 10
        else:
            answer += ageNum[age]
            break;

    return answer