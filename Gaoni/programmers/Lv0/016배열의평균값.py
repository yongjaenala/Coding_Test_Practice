def solution(numbers):
    answer = 0

    # answer = numbers[0]+(numbers[-1]-numbers[0])/2

    answer = sum(numbers) / len(numbers)
    return answer