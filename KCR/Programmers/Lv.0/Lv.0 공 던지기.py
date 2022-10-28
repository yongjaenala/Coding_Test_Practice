def solution(numbers, k):
    num = 0
    for i in range(2, k+1) :
        num += 2
        if num >= len(numbers) :
            num -= len(numbers)
        answer = numbers[num]
    return answer