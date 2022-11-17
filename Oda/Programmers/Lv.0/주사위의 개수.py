# box = [10,8,6]
# n = 3
#
# result = 1
# for i in box:
#     result *= i // n
#
# print(result)

def solution(box, n):
    answer = 1
    for i in box:
        answer *= i // n
    return answer