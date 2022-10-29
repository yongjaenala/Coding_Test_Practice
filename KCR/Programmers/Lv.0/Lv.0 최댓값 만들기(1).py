def solution(numbers):
    maxs = []
    for i in numbers :
        numbers.remove(i)
        maxs.append(max([i*n for n in numbers]))
        numbers.append(i)
    return max(maxs)