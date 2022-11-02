def solution(numbers):
    answer = 0

    for i in range(len(numbers)):
        answer += numbers[i]
    answer /= len(numbers)

    return answer

#------------------------------------------------
# def solution(numbers):
#     return sum(numbers) / len(numbers)

# import numpy as np
# def solution(numbers):
#     return np.mean(numbers)

