def solution(numbers, direction):
    if direction == 'left' :
        answer = numbers[1:]
        answer.append(numbers[0])
        return answer
    else :
        answer = numbers[:-1]
        answer.insert(0, numbers[-1])
        return answer