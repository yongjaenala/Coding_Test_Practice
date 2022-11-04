def solution(array):
    array.sort()
    answer = []
    result = []
    for i in array:
        if i not in answer:
            answer.append(i)
    for j in array:
        for x in answer:
            if x == j:
    return answer


array = [1,4,3,3,3,2]
print(array)
print(solution(array))