
def solution(numbers):
    answer = sorted(numbers, reverse=True)
    return answer[0] * answer[1]

def sol_sort(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]

def sol_sort2(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]