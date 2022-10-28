import string

def solution(age):
    lower = [i for i in string.ascii_lowercase]
    answer = ''
    while age:
        answer = lower[age % 10] + answer
        age = age // 10
    return answer

print(solution(23))