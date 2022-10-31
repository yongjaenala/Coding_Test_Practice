# https://school.programmers.co.kr/learn/courses/30/lessons/120834
# 외계행성의 나이
import string

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

# Gaon's Solution
# import string
#
# def solution(age):
#     lower = [i for i in string.ascii_lowercase]
#     answer = ''
#     while age:
#         answer = lower[age % 10] + answer
#         age = age // 10
#     return answer

# Chaerin's Solution
# def solution(age):
#     eng_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#     for i in str(age) :
#         answer = ''
#         for i in str(age) :
#             answer += eng_list[int(i)]
#         return answer