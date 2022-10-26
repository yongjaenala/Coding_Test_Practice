## 피자 나눠 먹기

import math

#-----------------(1)
def solution1(n):
    return math.ceil(n/7)


#-----------------(2)

import math


def solution2(n):
    answer = 0
    for i in range(max(n, 6), (n * 6) + 1):
        if i % n == 0 and i % 6 == 0:
            answer = i // 6
            break

    return answer

# import math
#
# def solution(n):
#     return (n * 6) // math.gcd(n, 6) // 6

#-----------------(3)

import math

def solution3(slice, n):
        return math.ceil(n/slice)

# def solution(slicen, n):
#     if n % slicen == 0:
#         answer = n // slicen
#     else:
#         answer = (n // slicen) + 1
#     return answer