# https://school.programmers.co.kr/learn/courses/30/lessons/120897
# 문자열 정렬하기 (1)

def solution(my_string):
    answer = []

    for str in my_string:
        try:
            answer.append(int(str))
        except:
            pass
    answer.sort()

    return answer



# 문제에서 answer을 오름차순으로 정렬하라고 한 지문을 확인하지 못해서 헤맸음