import re


def solution(my_string):
    # answer = 0
    num_l = list(map(int, re.findall(r'\d', my_string)))
    answer = sum(num_l)

    # print(num_l)
    return answer