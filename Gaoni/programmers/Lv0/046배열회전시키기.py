def solution(numbers, direction):
    if direction == 'left':
        num = numbers.pop(0)
        numbers.append(num)

    elif direction == 'right':
        num = numbers.pop(-1)
        numbers.insert(0, num)

    return numbers