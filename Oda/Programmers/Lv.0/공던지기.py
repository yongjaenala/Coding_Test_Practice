def solution(numbers, k):
    answer = 0

    temp = (k - 1) * 2 % len(numbers)
    answer = numbers[temp]

    return answer
