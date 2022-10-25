def solution(array, height):
    answer = len([x for x in array if x>height])

    return answer

print(solution([149, 180, 192, 170],199))