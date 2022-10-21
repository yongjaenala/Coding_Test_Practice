def solution(array):
    answer = 0

    array.sort()

    mid_num = len(array) // 2

    answer = array[mid_num]

    return answer