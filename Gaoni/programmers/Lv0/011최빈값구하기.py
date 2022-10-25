# import numpy as np
#
#
# def solution(array):
#     answer = 0
#
#     wonso = [0] * 1001
#
#     for i in array:
#         wonso[i] += 1
#
#     f_max_i = int(np.argmax(wonso))
#     s_max_i = int(np.argmax(wonso[f_max_i:])) + f_max_i + 1
#
#     f_max_v = wonso[f_max_i]
#     s_max_v = wonso[s_max_i]
#
#     if f_max_v == s_max_v:
#         answer = -1
#     else:
#         answer = f_max_i
#
#     #    print(wonso)
#     #    print(f_max)
#     #    print(s_max)
#
#     return answer
import numpy as np


def solution(array):
    answer = 0

    if len(array) == 1:
        answer = array[0]
    else:
        wonso = [0] * 1001

        for i in array:
            wonso[i] += 1

        f_max_i = int(np.argmax(wonso))

        if wonso[f_max_i] == wonso[int(np.argmax(wonso[f_max_i + 1:])) + f_max_i + 1]:
            answer = -1
        else:
            answer = f_max_i

    return answer
