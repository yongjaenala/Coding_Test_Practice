# 미완
# https://school.programmers.co.kr/learn/courses/30/lessons/120897
# 문자열 정렬하기 (1)

def solution(my_string):
    answer = []

    for str in my_string:
        try:
            answer.append(int(str))
        except:
            continue

    return answer

print(solution("hi12392"))