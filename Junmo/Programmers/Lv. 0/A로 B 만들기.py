# https://school.programmers.co.kr/learn/courses/30/lessons/120886
# A로 B 만들기

def solution(before, after):
    answer = 0

    temp1 = dict()
    temp2 = dict()
    for char in before:
        if temp1.get(char):
            temp1[char] += 1
        else:
            temp1[char] = 1
    for char in after:
        if temp2.get(char):
            temp2[char] += 1
        else:
            temp2[char] = 1
    if temp1 == temp2:
        answer = 1

    return answer